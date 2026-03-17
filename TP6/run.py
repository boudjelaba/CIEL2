from src.app import create_app

app = create_app()

# host=os.environ.get("POSTGRES_HOST", "postgres_db")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)