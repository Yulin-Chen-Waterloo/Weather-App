import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [city, setCity] = useState('');
    const [weather, setWeather] = useState(null);

    const getWeather = async () => {
        const response = await axios.get(`/weather/${city}`);
        setWeather(response.data);
    };

    return (
        <div>
            <input value={city} onChange={(e) => setCity(e.target.value)} placeholder="Enter city name" />
            <button onClick={getWeather}>Get Weather</button>
            {weather && <div>{/* Display the weather data here */}</div>}
        </div>
    );
}

export default App;
