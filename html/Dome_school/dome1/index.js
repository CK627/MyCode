document.addEventListener('DOMContentLoaded', function() {
    const pageEncoding = document.characterSet || document.charset;
    if (pageEncoding.toLowerCase() !== 'utf-8') {
        console.warn('页面编码不是UTF-8，可能导致中文显示异常');
    }
    
    const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');

    function switchTheme(e) {
        if (e.target.checked) {
            document.documentElement.classList.replace('light-mode', 'dark-mode');
            localStorage.setItem('theme', 'dark');
        } else {
            document.documentElement.classList.replace('dark-mode', 'light-mode');
            localStorage.setItem('theme', 'light');
        }    
    }

    toggleSwitch.addEventListener('change', switchTheme, false);

    const currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : 'light';

    if (currentTheme === 'dark') {
        document.documentElement.classList.replace('light-mode', 'dark-mode');
        toggleSwitch.checked = true;
    }

    const imageViewer = document.getElementById('imageViewer');
    const expandedImg = document.getElementById('expandedImg');
    const closeBtn = document.querySelector('.close-btn');

    const images = document.querySelectorAll('.read img');

    images.forEach(img => {
        img.style.cursor = 'pointer';
        img.addEventListener('click', function() {
            imageViewer.style.display = 'flex';
            expandedImg.src = this.src;
            document.body.style.overflow = 'hidden';
        });
    });

    closeBtn.addEventListener('click', function() {
        imageViewer.style.display = 'none';
        document.body.style.overflow = 'auto';
    });

    imageViewer.addEventListener('click', function(e) {
        if (e.target === imageViewer) {
            imageViewer.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });

    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && imageViewer.style.display === 'flex') {
            imageViewer.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });

    const viewCountElement = document.querySelector('.arti_views span');
    if (viewCountElement) {
        fetch('counter.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'increment=1'
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(count => {
            const numCount = parseInt(count);
            if (!isNaN(numCount)) {
                viewCountElement.textContent = numCount;
            }
        })
        .catch(error => {
            console.error('Error updating view count:', error);
            fetch('counter.php?get=1')
            .then(response => response.text())
            .then(count => {
                const numCount = parseInt(count);
                if (!isNaN(numCount)) {
                    viewCountElement.textContent = numCount;
                }
            })
            .catch(err => {
                console.error('Failed to get count:', err);
            });
        });
    }
}); 