document.addEventListener('DOMContentLoaded', function() {
    
    // ===============================================
    // 1. KARANLIK MOD (DARK MODE) AYARLARI
    // ===============================================
    
    const themeToggleBtn = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement; // <html> etiketini seçer
    
    // A) Daha önce seçilen bir tema var mı kontrol et
    const currentTheme = localStorage.getItem('theme');
    
    if (currentTheme) {
        htmlElement.setAttribute('data-theme', currentTheme);
        updateIcon(currentTheme);
    }
    
    // B) Butona tıklanınca ne olsun?
    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', function() {
            let theme = htmlElement.getAttribute('data-theme');
            
            if (theme === 'dark') {
                htmlElement.removeAttribute('data-theme'); // Light moda dön
                theme = 'light';
            } else {
                htmlElement.setAttribute('data-theme', 'dark'); // Dark moda geç
                theme = 'dark';
            }
            
            // Seçimi tarayıcıya kaydet
            localStorage.setItem('theme', theme);
            updateIcon(theme);
        });
    }

    // İkonu güncelleyen yardımcı fonksiyon
    function updateIcon(theme) {
        if (theme === 'dark') {
            themeToggleBtn.textContent = '☀️'; // Güneşe dön
        } else {
            themeToggleBtn.textContent = '🌙'; // Aya dön
        }
    }


    // ===============================================
    // 2. RESİM ÖNİZLEME (Sadece İçerik Ekle Sayfası İçin)
    // ===============================================
    
    const imageInput = document.getElementById('id_image');
    const previewContainer = document.getElementById('image-preview-container');
    const previewImage = document.getElementById('image-preview');

    if (imageInput) {
        imageInput.addEventListener('change', function(event) {
            const file = event.target.files[0];

            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    previewImage.src = e.target.result;
                    previewContainer.classList.remove('d-none');
                }
                reader.readAsDataURL(file);
            } else {
                previewImage.src = '#';
                previewContainer.classList.add('d-none');
            }
        });
    }
    // ===============================================
    // 3. BİLDİRİM (TOAST) SİSTEMİ
    // ===============================================
    
    // Sayfadaki tüm 'toast' sınıfına sahip elemanları bul
    var toastElList = [].slice.call(document.querySelectorAll('.toast'));
    
    // Hepsini Bootstrap Toast objesine çevir
    var toastList = toastElList.map(function (toastEl) {
        // delay: 5000 -> 5 saniye sonra kaybolur
        return new bootstrap.Toast(toastEl, { delay: 5000 }); 
    });
    
    // Hepsini göster
    toastList.forEach(function (toast) {
        toast.show();
    });

});