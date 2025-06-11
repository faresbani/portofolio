/**
 * Mobile Debug Helper
 * Add this script to any page to help debug mobile issues
 */

(function() {
    'use strict';
    
    // Create debug panel
    function createDebugPanel() {
        const panel = document.createElement('div');
        panel.id = 'mobile-debug-panel';
        panel.style.cssText = `
            position: fixed;
            top: 10px;
            right: 10px;
            background: rgba(0,0,0,0.9);
            color: white;
            padding: 15px;
            border-radius: 10px;
            font-family: monospace;
            font-size: 12px;
            z-index: 10000;
            max-width: 300px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            backdrop-filter: blur(10px);
        `;
        
        document.body.appendChild(panel);
        return panel;
    }
    
    // Get device information
    function getDeviceInfo() {
        const width = window.innerWidth;
        const height = window.innerHeight;
        const ratio = window.devicePixelRatio || 1;
        
        let deviceType = 'Desktop';
        let breakpoint = 'xl';
        
        if (width <= 576) {
            deviceType = 'Mobile';
            breakpoint = 'xs';
        } else if (width <= 768) {
            deviceType = 'Tablet Small';
            breakpoint = 'sm';
        } else if (width <= 992) {
            deviceType = 'Tablet Large';
            breakpoint = 'md';
        } else if (width <= 1200) {
            deviceType = 'Desktop Small';
            breakpoint = 'lg';
        }
        
        return {
            width,
            height,
            ratio,
            deviceType,
            breakpoint,
            orientation: width > height ? 'Landscape' : 'Portrait',
            touchDevice: 'ontouchstart' in window,
            userAgent: navigator.userAgent
        };
    }
    
    // Check for common mobile issues
    function checkMobileIssues() {
        const issues = [];
        
        // Check viewport meta tag
        const viewport = document.querySelector('meta[name="viewport"]');
        if (!viewport) {
            issues.push('❌ Missing viewport meta tag');
        } else if (!viewport.content.includes('width=device-width')) {
            issues.push('⚠️ Viewport not set to device-width');
        }
        
        // Check for horizontal scroll
        if (document.body.scrollWidth > window.innerWidth) {
            issues.push('❌ Horizontal scroll detected');
        }
        
        // Check for small touch targets
        const buttons = document.querySelectorAll('button, a, input[type="button"], input[type="submit"]');
        let smallTargets = 0;
        buttons.forEach(btn => {
            const rect = btn.getBoundingClientRect();
            if (rect.width < 44 || rect.height < 44) {
                smallTargets++;
            }
        });
        
        if (smallTargets > 0) {
            issues.push(`⚠️ ${smallTargets} small touch targets (<44px)`);
        }
        
        // Check for fixed elements that might cause issues
        const fixedElements = document.querySelectorAll('*');
        let problematicFixed = 0;
        fixedElements.forEach(el => {
            const style = window.getComputedStyle(el);
            if (style.position === 'fixed' && style.zIndex > 1000) {
                problematicFixed++;
            }
        });
        
        if (problematicFixed > 3) {
            issues.push(`⚠️ Many fixed elements (${problematicFixed})`);
        }
        
        return issues;
    }
    
    // Update debug panel
    function updateDebugPanel() {
        const panel = document.getElementById('mobile-debug-panel');
        if (!panel) return;
        
        const info = getDeviceInfo();
        const issues = checkMobileIssues();
        
        panel.innerHTML = `
            <div style="margin-bottom: 10px; font-weight: bold; color: #3498db;">
                📱 Mobile Debug Info
            </div>
            
            <div style="margin-bottom: 8px;">
                <strong>Device:</strong> ${info.deviceType}<br>
                <strong>Breakpoint:</strong> ${info.breakpoint}<br>
                <strong>Size:</strong> ${info.width}×${info.height}<br>
                <strong>Ratio:</strong> ${info.ratio}x<br>
                <strong>Orientation:</strong> ${info.orientation}<br>
                <strong>Touch:</strong> ${info.touchDevice ? 'Yes' : 'No'}
            </div>
            
            ${issues.length > 0 ? `
                <div style="margin-top: 10px; padding-top: 10px; border-top: 1px solid #555;">
                    <strong style="color: #e74c3c;">Issues Found:</strong><br>
                    ${issues.map(issue => `<div style="margin: 2px 0;">${issue}</div>`).join('')}
                </div>
            ` : `
                <div style="margin-top: 10px; padding-top: 10px; border-top: 1px solid #555; color: #27ae60;">
                    ✅ No issues detected
                </div>
            `}
            
            <div style="margin-top: 10px; padding-top: 10px; border-top: 1px solid #555;">
                <button onclick="this.parentElement.parentElement.style.display='none'" 
                        style="background: #e74c3c; color: white; border: none; padding: 5px 10px; border-radius: 5px; cursor: pointer;">
                    Close
                </button>
                <button onclick="window.mobileDebug.refresh()" 
                        style="background: #3498db; color: white; border: none; padding: 5px 10px; border-radius: 5px; cursor: pointer; margin-left: 5px;">
                    Refresh
                </button>
            </div>
        `;
    }
    
    // Performance monitoring
    function monitorPerformance() {
        const startTime = performance.now();
        
        window.addEventListener('load', () => {
            const loadTime = performance.now() - startTime;
            console.log(`📱 Mobile Debug: Page loaded in ${loadTime.toFixed(2)}ms`);
            
            // Check for large images
            const images = document.querySelectorAll('img');
            images.forEach(img => {
                if (img.naturalWidth > window.innerWidth * 2) {
                    console.warn(`📱 Mobile Debug: Large image detected: ${img.src}`);
                }
            });
        });
    }
    
    // Touch event debugging
    function debugTouchEvents() {
        let touchStartTime = 0;
        
        document.addEventListener('touchstart', (e) => {
            touchStartTime = Date.now();
            console.log('📱 Touch start:', e.touches.length, 'touches');
        });
        
        document.addEventListener('touchend', (e) => {
            const duration = Date.now() - touchStartTime;
            console.log(`📱 Touch end: ${duration}ms duration`);
        });
        
        // Detect scroll issues
        let lastScrollTop = 0;
        document.addEventListener('scroll', () => {
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            if (Math.abs(scrollTop - lastScrollTop) > 100) {
                console.log('📱 Large scroll jump detected');
            }
            lastScrollTop = scrollTop;
        });
    }
    
    // Initialize debug tools
    function init() {
        // Only run on mobile-sized screens or when forced
        if (window.innerWidth <= 768 || window.location.search.includes('mobile-debug')) {
            createDebugPanel();
            updateDebugPanel();
            monitorPerformance();
            debugTouchEvents();
            
            // Update on resize
            window.addEventListener('resize', updateDebugPanel);
            
            // Global access
            window.mobileDebug = {
                refresh: updateDebugPanel,
                info: getDeviceInfo,
                issues: checkMobileIssues
            };
            
            console.log('📱 Mobile Debug Tools Loaded');
            console.log('📱 Access via window.mobileDebug');
        }
    }
    
    // Auto-initialize
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
})();
