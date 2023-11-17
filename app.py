import timeit
from flask import Flask, request, jsonify, render_template
from linear_search import linear_search
from binary_search import binary_search
from exponential_search import exponential_search
from jump_search import jump_search
from interpolation_search import interpolation_search
from ternary_search import ternary_search
from data_set import generate_sorted_list

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    small_data = generate_sorted_list(100)
    medium_data = generate_sorted_list(1000)
    large_data = generate_sorted_list(10000)
    test_data = ", ".join(map(str, small_data)) # (modify) choose your desired data set in here
    #print(test_data)

    if request.method == "POST":
        array_str = request.form.get("array")
        target_str = request.form.get("target")
        search_type = request.form.get("search_type")

        try:
            array = list(map(int, array_str.split(",")))
            target = int(target_str)
            low, high = 0, len(array) - 1

            result = -1

            if search_type == "exponential":
                execution_time = timeit.timeit("exponential_search(array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = exponential_search(array, target)
            elif search_type == "binary":
                execution_time = timeit.timeit("binary_search(array, target, low, high)", globals={**globals(), "array": array, "target": target, "low": low, "high": high}, number=1) * 1000
                result = binary_search(array, target, low, high)
            elif search_type == "interpolation":
                execution_time = timeit.timeit("interpolation_search(array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = interpolation_search(array, target)
            elif search_type == "jump":
                execution_time = timeit.timeit("jump_search(array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = jump_search(array, target)
            elif search_type == "linear":
                execution_time = timeit.timeit("linear_search(array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = linear_search(array, target)
            elif search_type == "ternary":
                execution_time = timeit.timeit("ternary_search(array, target)", globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = ternary_search(array, target)

            return render_template("index.html", result=result, search_type=search_type, execution_time=execution_time, test_data=test_data)
        except ValueError:
            return render_template("index.html", error="Invalid input. Ensure the array and target are integers.")

    return render_template("index.html", test_data=test_data)

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()

    if not data or "array" not in data or "target" not in data:
        return jsonify({"error": "Invalid request data. Provide 'array' and 'target'."}), 400

    array = data["array"]
    target = data["target"]

    result_iterative = exponential_search(array, target)

    return jsonify({
        "iterative_search_result": result_iterative,
    })

if __name__ == "__main__":
    app.run(debug=True)
