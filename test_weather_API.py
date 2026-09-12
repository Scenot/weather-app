from weather_API import WeatherApp

def test_creates_table():
    app = WeatherApp("fake_key", "test_weather_db")
    app.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='search_history'")
    result = app.cursor.fetchone()

    assert result is not None
    app.close()

def test_saves_shows_history():
    app = WeatherApp("fake_key", "test_weather_db")
    app.save_history("Test_city", 23.2, "cloudy")

    app.cursor.execute("SELECT * FROM search_history WHERE city='Test_city'")
    result = app.cursor.fetchall()

    assert len(result) == 1
    assert result[0][1] == "Test_city"
    assert result[0][2] == 23.2
    app.close()