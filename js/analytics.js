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
            const analytics = this.getAnalytics();
            analytics.uniqueVisitors = new Set(analytics.uniqueVisitors);
            
            counterElement.innerHTML = `
                <div class="analytics-display">
                    <span class="counter-item">
                        <i class="bi bi-eye"></i> ${analytics.totalViews.toLocaleString()} مشاهدة
                    </span>
                    <span class="counter-item">
                        <i class="bi bi-people"></i> ${analytics.uniqueVisitors.size.toLocaleString()} زائر
                    </span>
                </div>
            `;
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
        display: flex;
        gap: 15px;
        align-items: center;
        font-size: 0.9rem;
        color: #666;
        margin: 10px 0;
    }
    
    .counter-item {
        display: flex;
        align-items: center;
        gap: 5px;
    }
    
    .counter-item i {
        color: var(--secondary-color, #3498db);
    }
    
    [data-theme="dark"] .analytics-display {
        color: #bdc3c7;
    }
    
    @media (max-width: 576px) {
        .analytics-display {
            flex-direction: column;
            gap: 8px;
            text-align: center;
        }
    }
`;
document.head.appendChild(style);

// Console commands for debugging
console.log(`
📊 Portfolio Analytics Loaded!

Available commands:
- portfolioAnalytics.getSummary() - View analytics summary
- portfolioAnalytics.exportData() - Download analytics data
- portfolioAnalytics.reset() - Reset all data

Current stats:`, analytics.getSummary());
