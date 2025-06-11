/**
 * Simple Analytics - Track page views without external services
 * This provides basic visitor tracking using localStorage
 */

class SimpleAnalytics {
    constructor() {
        this.storageKey = 'portfolio_analytics';
        this.sessionKey = 'portfolio_session';
        this.init();
    }

    init() {
        // Track page view when script loads
        this.trackPageView();
        
        // Track time spent on page
        this.startTime = Date.now();
        window.addEventListener('beforeunload', () => {
            this.trackTimeSpent();
        });
        
        // Track scroll depth
        this.maxScroll = 0;
        window.addEventListener('scroll', () => {
            this.trackScrollDepth();
        });
    }

    // Get or create visitor ID
    getVisitorId() {
        let visitorId = localStorage.getItem('visitor_id');
        if (!visitorId) {
            visitorId = 'visitor_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
            localStorage.setItem('visitor_id', visitorId);
        }
        return visitorId;
    }

    // Check if this is a new session
    isNewSession() {
        const sessionId = sessionStorage.getItem(this.sessionKey);
        if (!sessionId) {
            sessionStorage.setItem(this.sessionKey, Date.now().toString());
            return true;
        }
        return false;
    }

    // Get current analytics data
    getAnalytics() {
        const data = localStorage.getItem(this.storageKey);
        return data ? JSON.parse(data) : {
            totalViews: 0,
            uniqueVisitors: new Set(),
            pages: {},
            sessions: 0,
            firstVisit: Date.now(),
            lastVisit: Date.now()
        };
    }

    // Save analytics data
    saveAnalytics(data) {
        // Convert Set to Array for storage
        const saveData = {
            ...data,
            uniqueVisitors: Array.from(data.uniqueVisitors)
        };
        localStorage.setItem(this.storageKey, JSON.stringify(saveData));
    }

    // Track a page view
    trackPageView() {
        const analytics = this.getAnalytics();
        const page = window.location.pathname;
        const visitorId = this.getVisitorId();
        const isNewSession = this.isNewSession();

        // Convert array back to Set
        analytics.uniqueVisitors = new Set(analytics.uniqueVisitors);

        // Update counters
        analytics.totalViews++;
        analytics.uniqueVisitors.add(visitorId);
        analytics.lastVisit = Date.now();

        if (isNewSession) {
            analytics.sessions++;
        }

        // Track page-specific data
        if (!analytics.pages[page]) {
            analytics.pages[page] = {
                views: 0,
                uniqueViews: new Set(),
                totalTime: 0,
                bounceRate: 0
            };
        }

        analytics.pages[page].views++;
        analytics.pages[page].uniqueViews = new Set(analytics.pages[page].uniqueViews);
        analytics.pages[page].uniqueViews.add(visitorId);

        // Save data
        this.saveAnalytics(analytics);

        // Display counter if element exists
        this.displayCounter();

        // Log for debugging (remove in production)
        console.log('📊 Page view tracked:', {
            page,
            totalViews: analytics.totalViews,
            uniqueVisitors: analytics.uniqueVisitors.size,
            sessions: analytics.sessions
        });
    }

    // Track time spent on page
    trackTimeSpent() {
        const timeSpent = Date.now() - this.startTime;
        const analytics = this.getAnalytics();
        const page = window.location.pathname;

        analytics.uniqueVisitors = new Set(analytics.uniqueVisitors);

        if (analytics.pages[page]) {
            analytics.pages[page].totalTime += timeSpent;
            analytics.pages[page].uniqueViews = new Set(analytics.pages[page].uniqueViews);
        }

        this.saveAnalytics(analytics);
    }

    // Track scroll depth
    trackScrollDepth() {
        const scrollPercent = Math.round(
            (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100
        );
        
        if (scrollPercent > this.maxScroll) {
            this.maxScroll = scrollPercent;
        }
    }

    // Display visitor counter
    displayCounter() {
        const counterElement = document.getElementById('visitor-counter');
        if (counterElement) {
            try {
                const analytics = this.getAnalytics();
                analytics.uniqueVisitors = new Set(analytics.uniqueVisitors);

                // Calculate days since first visit
                const daysSinceStart = Math.floor((Date.now() - analytics.firstVisit) / (1000 * 60 * 60 * 24));
                const daysText = daysSinceStart === 0 ? 'اليوم' : `${daysSinceStart} يوم`;

                counterElement.innerHTML = `
                    <div class="analytics-display">
                        <div class="counter-stats">
                            <div class="counter-item">
                                <i class="bi bi-eye"></i>
                                <span class="counter-number">${analytics.totalViews.toLocaleString()}</span>
                                <span class="counter-label">مشاهدة</span>
                            </div>
                            <div class="counter-divider">•</div>
                            <div class="counter-item">
                                <i class="bi bi-people"></i>
                                <span class="counter-number">${analytics.uniqueVisitors.size.toLocaleString()}</span>
                                <span class="counter-label">زائر</span>
                            </div>
                            <div class="counter-divider">•</div>
                            <div class="counter-item">
                                <i class="bi bi-calendar-check"></i>
                                <span class="counter-number">${daysText}</span>
                                <span class="counter-label">منذ البداية</span>
                            </div>
                        </div>
                        <div class="counter-subtitle">
                            شكراً لزيارتكم موقعي الشخصي
                        </div>
                    </div>
                `;
            } catch (error) {
                console.error('Analytics display error:', error);
                // Fallback display
                counterElement.innerHTML = `
                    <div class="analytics-display">
                        <div class="counter-stats">
                            <div class="counter-item">
                                <i class="bi bi-eye"></i>
                                <span class="counter-number">1</span>
                                <span class="counter-label">مشاهدة</span>
                            </div>
                            <div class="counter-divider">•</div>
                            <div class="counter-item">
                                <i class="bi bi-people"></i>
                                <span class="counter-number">1</span>
                                <span class="counter-label">زائر</span>
                            </div>
                        </div>
                        <div class="counter-subtitle">
                            مرحباً بك في موقعي
                        </div>
                    </div>
                `;
            }
        }
    }

    // Get analytics summary
    getSummary() {
        const analytics = this.getAnalytics();
        analytics.uniqueVisitors = new Set(analytics.uniqueVisitors);

        // Convert pages data
        const pages = {};
        Object.keys(analytics.pages).forEach(page => {
            pages[page] = {
                ...analytics.pages[page],
                uniqueViews: new Set(analytics.pages[page].uniqueViews),
                avgTime: analytics.pages[page].totalTime / analytics.pages[page].views || 0
            };
        });

        return {
            totalViews: analytics.totalViews,
            uniqueVisitors: analytics.uniqueVisitors.size,
            sessions: analytics.sessions,
            pages: pages,
            firstVisit: new Date(analytics.firstVisit),
            lastVisit: new Date(analytics.lastVisit)
        };
    }

    // Export data (for backup or analysis)
    exportData() {
        const summary = this.getSummary();
        const dataStr = JSON.stringify(summary, null, 2);
        const dataBlob = new Blob([dataStr], {type: 'application/json'});
        
        const link = document.createElement('a');
        link.href = URL.createObjectURL(dataBlob);
        link.download = `portfolio-analytics-${new Date().toISOString().split('T')[0]}.json`;
        link.click();
    }

    // Reset all data
    reset() {
        localStorage.removeItem(this.storageKey);
        localStorage.removeItem('visitor_id');
        sessionStorage.removeItem(this.sessionKey);
        console.log('📊 Analytics data reset');
    }
}

// Initialize analytics
const analytics = new SimpleAnalytics();

// Make analytics available globally for debugging
window.portfolioAnalytics = analytics;

// Add CSS for counter display
const style = document.createElement('style');
style.textContent = `
    .analytics-display {
        text-align: center;
        padding: 15px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin: 10px 0;
    }

    .counter-stats {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
        margin-bottom: 8px;
        flex-wrap: wrap;
    }

    .counter-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 2px;
        min-width: 60px;
    }

    .counter-item i {
        font-size: 1.2rem;
        color: #3498db;
        margin-bottom: 2px;
    }

    .counter-number {
        font-size: 1.1rem;
        font-weight: bold;
        color: white;
        line-height: 1;
    }

    .counter-label {
        font-size: 0.75rem;
        color: rgba(255, 255, 255, 0.8);
        line-height: 1;
    }

    .counter-divider {
        color: rgba(255, 255, 255, 0.5);
        font-size: 1.2rem;
        margin: 0 5px;
    }

    .counter-subtitle {
        font-size: 0.8rem;
        color: rgba(255, 255, 255, 0.7);
        font-style: italic;
        margin-top: 5px;
    }

    /* Dark theme adjustments */
    [data-theme="dark"] .analytics-display {
        background: rgba(52, 73, 94, 0.3);
        border-color: rgba(255, 255, 255, 0.1);
    }

    [data-theme="dark"] .counter-item i {
        color: #5dade2;
    }

    /* Mobile responsive */
    @media (max-width: 768px) {
        .analytics-display {
            padding: 12px;
            margin: 15px 0;
        }

        .counter-stats {
            gap: 10px;
        }

        .counter-item {
            min-width: 50px;
        }

        .counter-number {
            font-size: 1rem;
        }

        .counter-label {
            font-size: 0.7rem;
        }

        .counter-subtitle {
            font-size: 0.75rem;
        }
    }

    @media (max-width: 576px) {
        .counter-stats {
            flex-direction: column;
            gap: 8px;
        }

        .counter-divider {
            display: none;
        }

        .counter-item {
            flex-direction: row;
            gap: 8px;
            min-width: auto;
        }

        .counter-item i {
            font-size: 1rem;
        }
    }
`;
document.head.appendChild(style);

// Initialize analytics when page loads
function initializeAnalytics() {
    try {
        if (typeof window.portfolioAnalytics === 'undefined') {
            window.portfolioAnalytics = new PortfolioAnalytics();
        }

        // Track page view
        window.portfolioAnalytics.trackPageView();

        // Display counter immediately
        window.portfolioAnalytics.displayCounter();

        // Update counter every 30 seconds
        setInterval(() => {
            window.portfolioAnalytics.displayCounter();
        }, 30000);

        console.log('✅ Analytics initialized successfully');
    } catch (error) {
        console.error('❌ Analytics initialization failed:', error);

        // Fallback: Show basic counter
        const counterElement = document.getElementById('visitor-counter');
        if (counterElement) {
            counterElement.innerHTML = `
                <div class="analytics-display">
                    <div class="counter-stats">
                        <div class="counter-item">
                            <i class="bi bi-eye"></i>
                            <span class="counter-number">1</span>
                            <span class="counter-label">مشاهدة</span>
                        </div>
                        <div class="counter-divider">•</div>
                        <div class="counter-item">
                            <i class="bi bi-people"></i>
                            <span class="counter-number">1</span>
                            <span class="counter-label">زائر</span>
                        </div>
                    </div>
                    <div class="counter-subtitle">
                        مرحباً بك في موقعي
                    </div>
                </div>
            `;
        }
    }
}

// Multiple initialization attempts to ensure it works
document.addEventListener('DOMContentLoaded', initializeAnalytics);

// Backup initialization
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeAnalytics);
} else {
    initializeAnalytics();
}

// Additional backup after window load
window.addEventListener('load', function() {
    setTimeout(initializeAnalytics, 100);
});

// Console commands for debugging
console.log(`
📊 Portfolio Analytics Loaded!

Available commands:
- portfolioAnalytics.getSummary() - View analytics summary
- portfolioAnalytics.exportData() - Download analytics data
- portfolioAnalytics.reset() - Reset all data
`);
