from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

def shuffle_meals(meal_ideas):
    random.shuffle(meal_ideas)
    return meal_ideas

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        meals = [request.form[f'meal_{i}'] for i in range(6)]
        if all(meal.strip() and not meal.isdigit() for meal in meals):
            meals.append("Treat Night - Visit or order from your favorite restaurant")
            shuffled_meals = shuffle_meals(meals)
            days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            meal_plan = list(zip(days_of_week, shuffled_meals))
            return render_template('result.html', meal_plan=meal_plan)
        else:
            return render_template('index.html', error="Invalid input: Meal ideas cannot be blank or contain only numbers. Please try again.")
    
    return render_template('index.html')

@app.route('/restart')
def restart():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)