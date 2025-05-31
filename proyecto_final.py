import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pickle
import os
from datetime import datetime, timedelta
import json

# Nodo para la lista enlazada que almacena el historial diario
class HistoryNode:
    def __init__(self, date, calories, exercise, weight):
        self.date = date
        self.calories = calories
        self.exercise = exercise  # minutos
        self.weight = weight
        self.next = None

    def __str__(self):
        return f"{self.date}: {self.weight}kg, {self.calories}kcal, {self.exercise}min"

# Lista enlazada para almacenar el historial diario del usuario
class HistoryLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_record(self, date, calories, exercise, weight):
        """Agrega un nuevo registro diario al historial."""
        new_node = HistoryNode(date, calories, exercise, weight)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def get_ml_data(self):
        """Obtiene los datos formateados para machine learning (X: [calorías, ejercicio], y: peso)."""
        if self.size < 2:
            return None, None

        x_data = []
        y_data = []
        current = self.head
        while current:
            x_data.append([current.calories, current.exercise])
            y_data.append(current.weight)
            current = current.next

        return np.array(x_data), np.array(y_data)

    def show_history(self, limit=10):
        """Muestra los registros más recientes del historial."""
        if self.size == 0:
            print("No hay registros de historial disponibles.")
            return

        print(f"\n--- Historial Reciente (últimos {min(limit, self.size)} registros) ---")
        current = self.head
        count = 0
        while current and count < limit:
            print(f"{count + 1}. {current}")
            current = current.next
            count += 1

    def get_last_weight(self):
        """Obtiene el último peso registrado."""
        if self.head:
            return self.head.weight
        return None

# Cola FIFO para gestionar hábitos saludables diarios
class HabitsQueue:
    def __init__(self):
        self.habits = [
            "Camina 30 minutos al aire libre",
            "Bebe 8 vasos de agua a lo largo del día",
            "Duerme 7-8 horas de calidad",
            "Come 5 porciones de frutas y verduras",
            "Haz 20 minutos de ejercicio cardiovascular",
            "Practica 10 minutos de meditación o relajación",
            "Evita bebidas azucaradas y refrescos",
            "Desayuna proteína en la primera hora del día",
            "Usa las escaleras en vez del ascensor",
            "Prepara comidas caseras en vez de comida rápida"
        ]
        self.current_index = 0

    def get_daily_habit(self):
        """Obtiene el hábito saludable de hoy (rotación FIFO)."""
        habit = self.habits[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.habits)
        return habit

    def add_custom_habit(self, habit):
        """Agrega un nuevo hábito personalizado."""
        self.habits.append(habit)

# Modelo de regresión lineal para predecir el peso
class WeightPredictionModel:
    def __init__(self):
        self.model = LinearRegression()
        self.scaler_x = StandardScaler()
        self.scaler_y = StandardScaler()
        self.trained = False
        self.model_file = "modelo_peso.pkl"

    def train(self, x_data, y_data):
        """Entrena el modelo con los datos históricos."""
        if len(x_data) < 3:
            print("Se requieren al menos 3 registros para entrenar el modelo.")
            return False

        # Normaliza los datos
        x_scaled = self.scaler_x.fit_transform(x_data)
        y_scaled = self.scaler_y.fit_transform(y_data.reshape(-1, 1)).ravel()

        # Entrena el modelo
        self.model.fit(x_scaled, y_scaled)
        self.trained = True

        # Calcula el error cuadrático medio
        predictions = self.model.predict(x_scaled)
        mse = np.mean((y_scaled - predictions) ** 2)
        print(f"Modelo entrenado. Error cuadrático medio: {mse:.4f}")

        return True

    def predict_weight(self, calories, exercise):
        """Predice el peso basado en calorías y ejercicio."""
        if not self.trained:
            return None

        input_data = np.array([[calories, exercise]])
        input_scaled = self.scaler_x.transform(input_data)
        prediction_scaled = self.model.predict(input_scaled)
        prediction = self.scaler_y.inverse_transform(prediction_scaled.reshape(-1, 1))[0][0]
        return prediction

    def get_coefficients(self):
        #Obtiene los coeficientes del modelo para interpretación
        if not self.trained:
            return None

        coefficients = self.model.coef_
        intercept = self.model.intercept_
        return {
            'calories': coefficients[0],
            'exercise': coefficients[1],
            'intercept': intercept
        }

    def save_model(self):
        #Guarda el modelo entrenado en disco
        if self.trained:
            with open(self.model_file, 'wb') as f:
                pickle.dump({
                    'model': self.model,
                    'scaler_x': self.scaler_x,
                    'scaler_y': self.scaler_y,
                    'trained': self.trained
                }, f)

    def load_model(self):
        #Carga un modelo previamente entrenado desde disco
        if os.path.exists(self.model_file):
            try:
                with open(self.model_file, 'rb') as f:
                    data = pickle.load(f)
                    self.model = data['model']
                    self.scaler_x = data['scaler_x']
                    self.scaler_y = data['scaler_y']
                    self.trained = data['trained']
                return True
            except:
                return False
        return False

# Clase principal de la aplicación de ayuda para bajar de peso
class WeightLossApp:
    def __init__(self):
        self.history = HistoryLinkedList()
        self.habits = HabitsQueue()
        self.model = WeightPredictionModel()
        self.data_file = "datos_usuario.json"
        self.load_data()
        self.model.load_model()

    def save_data(self):
        #Guarda el historial en un archivo JSON
        data = []
        current = self.history.head
        while current:
            data.append({
                'date': current.date,
                'calories': current.calories,
                'exercise': current.exercise,
                'weight': current.weight
            })
            current = current.next

        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)

    def load_data(self):
        #Carga el historial desde un archivo JSON
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                # Carga en orden inverso para mantener la estructura de la lista enlazada
                for record in reversed(data):
                    self.history.add_record(
                        record['date'],
                        record['calories'],
                        record['exercise'],
                        record['weight']
                    )
            except:
                print("Error al cargar los datos previos.")

    def add_daily_record(self):
        #Solicita al usuario agregar un nuevo registro diario
        print("\n--- Registro Diario ---")
        try:
            date = input("Fecha (AÑO-MES-DIA) o presiona Enter para registrar el día de hoy: ").strip()
            if not date:
                date = datetime.now().strftime("%Y-%m-%d")
            calories = float(input("Calorías consumidas: "))
            exercise = int(input("Minutos de ejercicio: "))
            weight = float(input("Peso actual (kg): "))
            self.history.add_record(date, calories, exercise, weight)
            print(f"Registro agregado correctamente para {date}")
        except ValueError:
            print("Error: Por favor ingresa valores numéricos válidos.")

    def show_daily_habit(self):
        """Muestra el hábito saludable del día."""
        habit = self.habits.get_daily_habit()
        print(f"\nHábito saludable de hoy: {habit}")
        return habit

    def train_prediction_model(self):
        #Entrena el modelo de predicción de peso
        print("\n--- Entrenando el Modelo de Predicción ---")
        x_data, y_data = self.history.get_ml_data()
        if x_data is None:
            print("Se requieren al menos 2 registros para entrenar el modelo.")
            return False
        if self.model.train(x_data, y_data):
            self.model.save_model()
            print("Modelo entrenado y guardado correctamente.")
            return True
        return False

    def make_prediction(self):
        #Realiza una predicción de peso según los datos ingresados por el usuario
        if not self.model.trained:
            print("El modelo no está entrenado. Por favor, entrena el modelo primero.")
            return

        print("\n--- Predicción de Peso ---")
        try:
            calories = float(input("Calorías planificadas: "))
            exercise = int(input("Minutos de ejercicio planificados: "))
            predicted_weight = self.model.predict_weight(calories, exercise)
            current_weight = self.history.get_last_weight()
            print(f"\nPeso predicho: {predicted_weight:.2f} kg")
            if current_weight:
                diff = predicted_weight - current_weight
                if diff > 0:
                    print(f"Posible aumento de peso de {diff:.2f} kg")
                else:
                    print(f"Posible pérdida de peso de {abs(diff):.2f} kg")
            # Mostrar recomendaciones personalizadas
            self.show_recommendations(calories, exercise)
        except ValueError:
            print("Error: Por favor ingresa valores numéricos válidos.")

    def show_recommendations(self, calories, exercise):
        #Muestra recomendaciones personalizadas según los coeficientes del modelo y los datos ingresados
        coefficients = self.model.get_coefficients()
        if not coefficients:
            return
        print("\nRecomendaciones personalizadas:")
        # Recomendaciones según los coeficientes del modelo
        if coefficients['calories'] > 0:
            print("• Reducir la ingesta calórica puede ayudar a perder peso")
        else:
            print("• Mantén una ingesta calórica adecuada")
        if coefficients['exercise'] < 0:
            print("• Aumentar el ejercicio puede acelerar la pérdida de peso")
        else:
            print("• Mantén tu rutina de ejercicio actual")
        # Recomendaciones específicas
        if calories > 2000:
            print("• Considera reducir las calorías a 1800-2000 por día")
        if exercise < 30:
            print("• Intenta realizar al menos 30 minutos de ejercicio diario")
        print("• Sé constante con tus hábitos saludables")

    def show_progress_analysis(self):
        #Muestra un análisis del progreso de pérdida de peso del usuario
        if self.history.size < 2:
            print("Se requieren al menos 2 registros para mostrar el progreso.")
            return

        print("\n--- Análisis de Progreso ---")
        # Recolecta los datos para el análisis
        data = []
        current = self.history.head
        while current:
            data.append({
                'date': current.date,
                'weight': current.weight,
                'calories': current.calories,
                'exercise': current.exercise
            })
            current = current.next
        # Ordena por fecha
        data.sort(key=lambda x: x['date'])
        # Calcula estadísticas
        initial_weight = data[0]['weight']
        current_weight = data[-1]['weight']
        total_loss = initial_weight - current_weight
        avg_calories = np.mean([d['calories'] for d in data])
        avg_exercise = np.mean([d['exercise'] for d in data])
        print(f"Peso inicial: {initial_weight:.1f} kg")
        print(f"Peso actual: {current_weight:.1f} kg")
        print(f"Cambio total: {total_loss:+.1f} kg")
        print(f"Promedio de calorías: {avg_calories:.0f} kcal/día")
        print(f"Promedio de ejercicio: {avg_exercise:.0f} min/día")
        if total_loss > 0:
            print("¡Felicidades! Estás perdiendo peso.")
        elif total_loss < 0:
            print("Has aumentado de peso. Considera ajustar tu plan.")
        else:
            print("Tu peso se mantiene estable.")

    def main_menu(self):
        #Muestra el menú principal y gestiona la interacción con el usuario
        while True:
            print("\n" + "="*50)
            print("Bajar de peso")
            print("="*50)
            print("1. Agregar registro diario")
            print("2. Ver historial")
            print("3. Ver hábito de hoy")
            print("4. Entrenar modelo de predicción")
            print("5. Realizar predicción de peso")
            print("6. Análisis de progreso")
            print("7. Agregar hábito personalizado")
            print("8. Guardar y salir")
            print("-" * 50)
            try:
                option = input("Selecciona una opción (1-8): ").strip()
                if option == '1':
                    self.add_daily_record()
                    self.save_data()
                elif option == '2':
                    self.history.show_history()
                elif option == '3':
                    self.show_daily_habit()
                elif option == '4':
                    self.train_prediction_model()
                elif option == '5':
                    self.make_prediction()
                elif option == '6':
                    self.show_progress_analysis()
                elif option == '7':
                    habit = input("Ingresa un nuevo hábito saludable: ").strip()
                    if habit:
                        self.habits.add_custom_habit(habit)
                        print("Hábito agregado correctamente.")
                elif option == '8':
                    self.save_data()
                    print("Datos guardados!")
                    break
                else:
                    print("Opción no válida. Intenta de nuevo.")
            except KeyboardInterrupt:
                print("\nGuardando datos antes de salir...")
                self.save_data()
                print("¡Hasta luego!")
                break
            except Exception as e:
                print(f"Error inesperado: {e}")

def main():
    #Funciones Principales
    print("Bienvenido/a")
    print("• Registrar tu progreso diario")
    print("• Recibir hábitos saludables")
    print("• Predecir la evolución de tu peso")
    print("• Obtener recomendaciones personalizadas")
    app = WeightLossApp()
    app.main_menu()

if __name__ == "__main__":
    main()
