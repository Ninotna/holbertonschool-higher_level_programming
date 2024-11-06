from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json_file(filepath):
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return {"error": str(e)}


def read_csv_file(filepath):
    data = []
    try:
        with open(filepath, "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                data.append(row)
    except FileNotFoundError as e:
        return {"error": str(e)}
    except ValueError as e:
        return {"error": f"Data parsing error: {e}"}
    return data


@app.route("/products")
def display_products():
    source = request.args.get("source")
    product_id = request.args.get("id", type=int)

    if source == "json":
        products = read_json_file("products.json")
    elif source == "csv":
        products = read_csv_file("products.csv")
    else:
        return render_template("product_display.html", error_message="Wrong source")

    if isinstance(products, dict) and "error" in products:
        return render_template("product_display.html", error_message=products["error"])

    if product_id:
        products = [product for product in products if product.get("id") == product_id]
        if not products:
            return render_template(
                "product_display.html", error_message="Product not found"
            )

    return render_template("product_display.html", products=products)


if __name__ == "__main__":
    app.run(debug=True)
