// Sayfa tamamen yüklendiğinde çalışması için DOMContentLoaded ekliyoruz
document.addEventListener('DOMContentLoaded', function() {
    
    // Django'nun varsayılan ID'si 'id_image'dir.
    // Eğer formda field adı farklıysa burayı güncellemelisin.
    const imageInput = document.getElementById('id_image');
    const previewContainer = document.getElementById('image-preview-container');
    const previewImage = document.getElementById('image-preview');

    // Eğer input elementi sayfada varsa (Hata almamak için kontrol)
    if (imageInput) {
        imageInput.addEventListener('change', function(event) {
            const file = event.target.files[0];

            if (file) {
                const reader = new FileReader();

                reader.onload = function(e) {
                    previewImage.src = e.target.result;
                    // Bootstrap'ın d-none (display:none) sınıfını kaldır
                    previewContainer.classList.remove('d-none');
                }

                reader.readAsDataURL(file);
            } else {
                previewImage.src = '#';
                previewContainer.classList.add('d-none');
            }
        });
    }
});