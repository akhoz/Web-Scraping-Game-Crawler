# 🎮 Game Price Comparison Web Scraper

A full-stack web application that automates the process of finding the best game deals across multiple online stores. Built with Vue.js and Scrapy, this project delivers real-time price comparisons in an intuitive storefront interface.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Vue.js](https://img.shields.io/badge/Vue.js-3.2+-brightgreen.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey.svg)
![Scrapy](https://img.shields.io/badge/Scrapy-2.5+-red.svg)

## 📋 Overview

This application solves the common problem of comparing video game prices across different online retailers. Instead of manually checking multiple websites, users can view all pricing information in one centralized interface. The system automatically scrapes and updates game prices from major retailers, providing users with the most cost-effective purchasing options.

### Key Features

- 🔍 **Multi-Platform Price Scraping**: Automatically collects pricing data from G2A, Instant Gaming, PlayStation Store, Metacritic, and HowLongToBeat
- 💰 **Real-Time Price Comparison**: Displays current prices and discounts across all platforms
- 🎨 **Modern UI**: Clean, responsive storefront interface built with Vue.js and Element Plus
- 📊 **Game Metadata**: Includes ratings, playtime estimates, and detailed game information
- ⚡ **RESTful API**: Flask backend provides structured API endpoints for game data
- 🔄 **Automated Updates**: Scrapy spiders can be scheduled to refresh pricing data periodically

## 🏗️ Architecture

### Frontend
- **Framework**: Vue.js 3 with TypeScript
- **UI Library**: Element Plus, Bootstrap 5
- **Routing**: Vue Router 4
- **HTTP Client**: Axios
- **Styling**: Custom CSS with responsive design

### Backend
- **Web Framework**: Flask with CORS support
- **Web Scraping**: Scrapy framework with custom spiders
- **Data Storage**: JSON-based lightweight database
- **API**: RESTful endpoints for game data retrieval

### Web Scrapers
Custom Scrapy spiders for each platform:
- **G2A Spider**: Scrapes prices, discounts, and product links
- **Instant Gaming Spider**: Collects pricing and availability data
- **PlayStation Store Spider**: Extracts console game pricing
- **Metacritic Spider**: Gathers game ratings and reviews
- **HowLongToBeat Spider**: Retrieves average playtime statistics

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- npm or yarn package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/akhoz/Web-Scraping-Game-Crawler.git
   cd Web-Scraping-Game-Crawler
   ```

2. **Set up the Python backend**
   ```bash
   # Install Python dependencies
   pip install flask flask-cors scrapy
   ```

3. **Set up the Vue.js frontend**
   ```bash
   cd frontend
   npm install
   ```

### Running the Application

1. **Start the Flask backend server**
   ```bash
   # From the project root directory
   python main.py
   ```
   The API will be available at `http://localhost:5000`

2. **Launch the Vue.js development server**
   ```bash
   cd frontend
   npm run serve
   ```
   The frontend will be available at `http://localhost:8080`

3. **Run the web scrapers (optional)**
   ```bash
   cd GameCrawler/GameCrawler
   
   # Run individual spiders
   scrapy crawl g2a
   scrapy crawl instantGaming
   scrapy crawl playStation
   scrapy crawl metacritic
   scrapy crawl howlongtobeat
   ```

## 📁 Project Structure

```
Web-Scraping-Game-Crawler/
├── main.py                      # Flask API server
├── GameCrawler/                 # Scrapy project
│   └── GameCrawler/
│       ├── spiders/             # Custom web scrapers
│       │   ├── g2a.py
│       │   ├── instantGaming.py
│       │   ├── playStation.py
│       │   ├── metacritic.py
│       │   └── howlongtobeat.py
│       ├── items.py             # Data models
│       ├── pipelines.py         # Data processing
│       ├── settings.py          # Scraper configuration
│       └── data.json            # Scraped data storage
└── frontend/                    # Vue.js application
    ├── src/
    │   ├── components/          # Vue components
    │   │   └── GameCard.vue
    │   ├── views/               # Page views
    │   │   ├── HomeView.vue
    │   │   ├── GameDetailView.vue
    │   │   └── AboutView.vue
    │   ├── router/              # Route configuration
    │   ├── App.vue              # Root component
    │   └── main.ts              # Application entry
    └── package.json             # Frontend dependencies
```

## 🔌 API Endpoints

### Get All Games
```http
GET /games
```
Returns a list of all games with pricing information from all scraped platforms.

**Response Example:**
```json
[
  {
    "id": 1,
    "game_name": "Elden Ring",
    "game_price": "€39.99",
    "game_rating": "9.5",
    "game_hours": "55",
    "platform": "G2A",
    "discount": "33%"
  }
]
```

### Get Game by ID
```http
GET /games/:id
```
Returns detailed information for a specific game.

## 🛠️ Technologies Used

**Frontend:**
- Vue.js 3
- TypeScript
- Vue Router
- Axios
- Element Plus
- Bootstrap 5

**Backend:**
- Python 3.8+
- Flask
- Flask-CORS
- Scrapy
- JSON

**Tools & Practices:**
- RESTful API design
- Web scraping with XPath selectors
- Responsive design
- Component-based architecture
- TypeScript for type safety

## 💡 Key Learnings & Achievements

- Developed custom Scrapy spiders to handle dynamic web content across different site structures
- Implemented efficient data aggregation from multiple sources
- Created a responsive single-page application with Vue.js
- Designed and implemented a RESTful API with Flask
- Managed state and routing in a modern JavaScript framework
- Applied web scraping best practices including error handling and rate limiting

## 🔮 Future Enhancements

- [ ] Add user authentication and saved game lists
- [ ] Implement price history tracking and charts
- [ ] Add email notifications for price drops
- [ ] Expand to include more gaming platforms (Steam, Epic Games, etc.)
- [ ] Implement a PostgreSQL database for better scalability
- [ ] Add automated scraping with scheduled tasks (Celery/Redis)
- [ ] Create price prediction using historical data
- [ ] Add filters and advanced search functionality

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

⭐ If you found this project interesting, please consider giving it a star!
