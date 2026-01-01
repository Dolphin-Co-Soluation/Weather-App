// DOM Elements
const cityInput = document.getElementById('cityInput');
const searchBtn = document.getElementById('searchBtn');
const errorMsg = document.getElementById('errorMsg');
const weatherDisplay = document.getElementById('weatherDisplay');
const welcomeState = document.getElementById('welcomeState');
const loadingSpinner = document.getElementById('loadingSpinner');
const forecastContainer = document.getElementById('forecastContainer');
const hourlyForecast = document.getElementById('hourlyForecast');
const forecastDate = document.getElementById('forecastDate');

// Weather Icon Mapping
const iconMap = {
    '01d': '☀️', '01n': '🌙',
    '02d': '⛅', '02n': '☁️',
    '03d': '☁️', '03n': '☁️',
    '04d': '☁️', '04n': '☁️',
    '09d': '🌧️', '09n': '🌧️',
    '10d': '🌦️', '10n': '🌧️',
    '11d': '⛈️', '11n': '⛈️',
    '13d': '❄️', '13n': '❄️',
    '50d': '🌫️', '50n': '🌫️'
};

// Weather Condition Groups
const weatherGroups = {
    sunny: ['01d', '02d'],
    cloudy: ['03d', '04d', '02n'],
    rainy: ['09d', '10d', '09n', '10n'],
    stormy: ['11d', '11n'],
    snowy: ['13d', '13n'],
    foggy: ['50d', '50n']
};

// Event Listeners
searchBtn.addEventListener('click', () => searchWeather());
cityInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') searchWeather();
});

// Search Weather Function
async function searchWeather() {
    const city = cityInput.value.trim();

    if (!city) {
        showError('Please enter a city name');
        return;
    }

    clearError();
    showLoading();

    try {
        const response = await fetch(`/api/weather?city=${encodeURIComponent(city)}`);
        const data = await response.json();

        if (!response.ok) {
            showError(data.error || 'Failed to fetch weather data');
            hideLoading();
            return;
        }

        displayWeather(data);
        fetchForecast(city);
        hideLoading();
    } catch (error) {
        console.error('Error:', error);
        showError('Network error. Please check your connection and try again.');
        hideLoading();
    }
}

// Display Weather Data
function displayWeather(weather) {
    try {
        document.getElementById('cityName').textContent = 
            `${weather['city']}, ${weather['country']}`;
        document.getElementById('weatherDescription').textContent = 
            weather['description'];
        document.getElementById('temperatureLarge').textContent = 
            `${Math.round(weather['temperature'])}°`;
        document.getElementById('precipitation').textContent = 
            `${weather['humidity']}%`;
        
        // Safe property access
        const maxTemp = weather['feels_like'] ? Math.round(weather['feels_like']) : Math.round(weather['temperature']);
        const minTemp = Math.round(weather['temperature'] - 2); // Estimate
        
        document.getElementById('tempRange').textContent = 
            `${maxTemp}°/${minTemp}°`;
        document.getElementById('humidityValue').textContent = 
            `${weather['humidity']}%`;
        document.getElementById('windSpeedValue').textContent = 
            `${weather['wind_speed'].toFixed(1)} m/s`;
        
        // Set Weather Icon
        const iconCode = weather['icon'];
        document.getElementById('weatherIconLarge').textContent = 
            iconMap[iconCode] || '🌤️';
        
        // Display Local Time
        if (weather['local_time_short']) {
            document.getElementById('localTime').textContent = weather['local_time_short'];
        }
        
        // Set date
        const now = new Date();
        forecastDate.textContent = now.toLocaleDateString('en-US', { 
            weekday: 'long',
            month: 'short',
            day: 'numeric'
        });

        // Show Weather Display and Hide Welcome State
        weatherDisplay.style.display = 'block';
        welcomeState.style.display = 'none';
        
        // Trigger card animations
        animateCards();
    } catch (error) {
        console.error('Error displaying weather:', error);
        showError('Error displaying weather data');
    }
}

// Animate cards when they appear
function animateCards() {
    const infoBoxes = document.querySelectorAll('.info-box');
    const forecastCards = document.querySelectorAll('.forecast-card');
    const infoSections = document.querySelectorAll('.info-section');
    
    // Add animation class to info boxes
    infoBoxes.forEach((box, index) => {
        box.style.animation = `slideUp 0.5s ease-out backwards`;
        box.style.animationDelay = `${0.1 + index * 0.05}s`;
    });
    
    // Add animation class to forecast cards
    forecastCards.forEach((card, index) => {
        card.style.animation = `slideUp 0.5s ease-out backwards`;
        card.style.animationDelay = `${0.2 + index * 0.05}s`;
    });
    
    // Add animation class to info sections
    infoSections.forEach((section, index) => {
        section.style.animation = `slideUp 0.6s ease-out backwards`;
        section.style.animationDelay = `${0.35 + index * 0.05}s`;
    });
}

// Update Background Animation
function updateBackground(iconCode) {
    // No background animation needed for new design
}

// Fetch Forecast
async function fetchForecast(city) {
    try {
        const response = await fetch(`/api/forecast?city=${encodeURIComponent(city)}`);
        const data = await response.json();

        if (response.ok && data.forecast) {
            displayForecast(data.forecast);
        }
    } catch (error) {
        console.error('Error fetching forecast:', error);
    }
}

// Display Forecast
function displayForecast(forecast) {
    forecastContainer.innerHTML = '';

    forecast.slice(0, 5).forEach((day, index) => {
        const card = document.createElement('div');
        card.className = 'forecast-card';
        card.style.animationDelay = `${index * 0.1}s`;

        const date = new Date(day.date).toLocaleDateString('en-US', {
            weekday: 'short'
        });

        const icon = iconMap[day.icon] || '🌤️';

        card.innerHTML = `
            <div class="forecast-day">${date}</div>
            <div class="forecast-icon">${icon}</div>
            <div class="forecast-temp">${Math.round(day.temperature)}°</div>
            <div class="forecast-desc">${day.description.substring(0, 10)}</div>
        `;

        forecastContainer.appendChild(card);
    });
}

// Utility Functions
function showError(message) {
    errorMsg.textContent = message;
    errorMsg.style.display = 'block';
}

function clearError() {
    errorMsg.textContent = '';
    errorMsg.style.display = 'none';
}

function showLoading() {
    loadingSpinner.style.display = 'flex';
    weatherDisplay.style.display = 'none';
    welcomeState.style.display = 'none';
}

function hideLoading() {
    loadingSpinner.style.display = 'none';
}

// Particle Animation System
class Particle {
    constructor(x, y, type = 'rain') {
        this.x = x;
        this.y = y;
        this.type = type;
        this.vx = (Math.random() - 0.5) * 4;
        this.vy = Math.random() * 2 + 2;
        this.opacity = 1;
        this.life = 100;
    }

    update() {
        this.x += this.vx;
        this.y += this.vy;
        this.life -= 1;
        this.opacity = this.life / 100;
    }
}

let particles = [];
let animationFrameId = null;

function createParticles(iconCode) {
    particles = [];
    const container = weatherBg;
    const width = container.offsetWidth;
    const height = container.offsetHeight;

    if (weatherGroups.rainy.includes(iconCode)) {
        for (let i = 0; i < 30; i++) {
            particles.push(new Particle(
                Math.random() * width,
                Math.random() * height,
                'rain'
            ));
        }
    } else if (weatherGroups.snowy.includes(iconCode)) {
        for (let i = 0; i < 20; i++) {
            particles.push(new Particle(
                Math.random() * width,
                Math.random() * height,
                'snow'
            ));
        }
    } else if (weatherGroups.stormy.includes(iconCode)) {
        for (let i = 0; i < 50; i++) {
            particles.push(new Particle(
                Math.random() * width,
                Math.random() * height,
                'storm'
            ));
        }
    }

    animateParticles();
}

function animateParticles() {
    const container = weatherBg;
    const width = container.offsetWidth;
    const height = container.offsetHeight;

    particles.forEach((p, index) => {
        p.update();

        if (p.life <= 0) {
            particles.splice(index, 1);
        } else if (p.y > height) {
            p.y = -10;
            p.x = Math.random() * width;
        }
    });

    if (particles.length > 0) {
        animationFrameId = requestAnimationFrame(animateParticles);
    }
}

// Allow user to see initial state on page load
window.addEventListener('load', () => {
    welcomeState.style.display = 'flex';
    weatherDisplay.style.display = 'none';
    addWelcomeAnimation();
});

// Add welcome animation
function addWelcomeAnimation() {
    const emoji = document.querySelector('.welcome-icon');
    if (emoji) {
        emoji.style.animation = 'bounce 2s ease-in-out infinite';
    }
}

// Add pulse effect to search button
function addSearchPulse() {
    const btn = document.getElementById('searchBtn');
    if (btn) {
        btn.style.animation = 'pulse 2s ease-in-out infinite';
    }
}

addSearchPulse();
