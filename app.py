""" Laboratory Management
    Developed by: Luiz Marin
"""
from lab_manager import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)