📺 YouTube Downloader Pro v4.0 - Ultimate Edition

<!-- Language Navigation -->

<p align="center">
<a href="#-türkçe">🇹🇷 Türkçe</a> •
<a href="#-english">🇬🇧 English</a>
</p>

🇹🇷 Türkçe

YouTube Downloader Pro, medya içeriklerini en yüksek kalitede ve en optimize formatlarda cihazınıza kaydetmek için tasarlanmış, açık kaynaklı bir masaüstü uygulamasıdır. Gücünü endüstri standardı yt-dlp motorundan alan bu yazılım, modern Tkinter arayüzü ile son kullanıcıya karmaşık komut satırı işlemleri olmadan profesyonel bir deneyim sunar.

🚀 Proje Hakkında

Bu proje, standart video indirme araçlarının aksine performans, kullanıcı deneyimi (UX) ve sürdürülebilirlik odaklı geliştirilmiştir. Arka planda çalışan akıllı algoritmalar sayesinde, video ve ses dosyaları kalite kaybı yaşanmadan (lossless extraction) işlenir.

Neden YouTube Downloader Pro?

FFmpeg Bağımlılığı Yok: Yerleşik "non-merge" modu sayesinde harici kodek kurulumlarına ihtiyaç duymadan çalışır.

Thread-Safe Mimari: Arayüz (GUI) ve indirme işlemleri ayrı iş parçacıklarında (threading) çalışarak uygulamanın donmasını engeller.

Akıllı Hata Yönetimi: Ağ kopmaları veya geçersiz link durumlarında kullanıcıyı bilgilendiren sağlam (robust) bir yapıya sahiptir.

🌟 Temel Özellikler

Özellik

Açıklama

🎬 Akıllı Çözünürlük

Videoları MP4 formatında, mevcut en iyi bit-rate ile indirir.

🎵 Hi-Fi Ses Modu

Görüntüden bağımsız, saf ses dosyası (M4A/AAC) olarak dışa aktarım sağlar.

🖼️ Meta Veri Analizi

URL girildiği an video başlığı, kapak resmi (thumbnail) ve süre bilgisini çeker.

📊 Canlı Telemetri

İndirme hızını, dosya boyutunu ve kalan süreyi (ETA) milisaniye hassasiyetinde gösterir.

📋 Clipboard Entegrasyonu

Panodaki linki otomatik algılar, analiz eder ve indirmeye hazırlar.

📂 Dinamik Dosya Yönetimi

İndirme konumunu özelleştirme ve işlem sonrası otomatik dizin erişimi sunar.

🛠️ Kurulum ve Yapılandırma

Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları takip ediniz.

Ön Gereksinimler

Python 3.8 veya daha yeni bir sürüm.

İnternet bağlantısı.

Adım 1: Bağımlılıkların Yüklenmesi

Terminal veya Komut İstemi (CMD) üzerinden gerekli kütüphaneleri yükleyin:

pip install yt-dlp Pillow


Adım 2: Uygulamanın Başlatılması

Proje dizinine gidin ve uygulamayı çalıştırın:

python youtube_indirici.py


🖥️ Kullanım Senaryosu

Bağlantı Girişi: YouTube video URL'sini kopyalayın.

Otomatik Analiz: Uygulamadaki "Yapıştır & Analiz Et" butonuna tıklayın. Yazılım, videonun meta verilerini ve kapak görselini ekrana getirecektir.

Format Belirleme: İhtiyacınıza göre Video (MP4) veya Sadece Ses seçeneğini işaretleyin.

İşlem Başlatma: "İndirmeyi Başlat" butonuna basın ve ilerleme çubuğundan süreci takip edin.

Sonuç: İşlem tamamlandığında "Klasörü Aç" butonu ile dosyaya doğrudan erişin.

⚖️ Lisans ve Yasal Uyarı

Bu proje MIT Lisansı ile lisanslanmıştır.

Yasal Uyarı: Bu yazılım yalnızca eğitim ve kişisel arşivleme amaçlı geliştirilmiştir. Telif hakkı ile korunan materyallerin izinsiz indirilmesi ve dağıtılması, YouTube Hizmet Koşulları'na ve yerel yasalarımıza aykırı olabilir. Kullanıcı, yazılımın kullanımından doğacak her türlü yasal sorumluluğu kabul etmiş sayılır.

🇬🇧 English

YouTube Downloader Pro is an open-source desktop application designed to save media content to your device in the highest quality and most optimized formats. Powered by the industry-standard yt-dlp engine, this software offers a professional experience with a modern Tkinter interface, eliminating the need for complex command-line operations.

🚀 About the Project

Unlike standard video downloading tools, this project is developed with a focus on performance, user experience (UX), and sustainability. Thanks to smart algorithms running in the background, video and audio files are processed without quality loss (lossless extraction).

Why YouTube Downloader Pro?

No FFmpeg Dependency: Works without needing external codec installations thanks to the built-in "non-merge" mode.

Thread-Safe Architecture: The interface (GUI) and download processes run on separate threads, preventing the application from freezing.

Smart Error Management: Has a robust structure that informs the user in case of network disconnections or invalid links.

🌟 Key Features

Feature

Description

🎬 Smart Resolution

Downloads videos in MP4 format with the best available bit-rate.

🎵 Hi-Fi Audio Mode

Exports pure audio files (M4A/AAC) independent of the video.

🖼️ Metadata Analysis

Fetches video title, thumbnail, and duration as soon as the URL is entered.

📊 Live Telemetry

Displays download speed, file size, and remaining time (ETA) with millisecond precision.

📋 Clipboard Integration

Automatically detects the link in the clipboard, analyzes it, and prepares it for download.

📂 Dynamic File Management

Offers customization of download location and automatic directory access after processing.

🛠️ Installation and Configuration

Follow the steps below to run the project in your local environment.

Prerequisites

Python 3.8 or newer.

Internet connection.

Step 1: Installing Dependencies

Install the required libraries via Terminal or Command Prompt (CMD):

pip install yt-dlp Pillow


Step 2: Launching the Application

Navigate to the project directory and run the application:

python youtube_indirici.py


🖥️ Usage Scenario

Input Link: Copy the YouTube video URL.

Auto Analysis: Click the "Paste & Analyze" button in the app. The software will display the video metadata and thumbnail.

Select Format: Choose Video (MP4) or Audio Only according to your needs.

Start Process: Click the "Start Download" button and follow the process on the progress bar.

Result: When the process is complete, access the file directly with the "Open Folder" button.

⚖️ License and Legal Disclaimer

This project is licensed under the MIT License.

Legal Disclaimer: This software is developed for educational and personal archiving purposes only. Unauthorized downloading and distribution of copyrighted materials may violate YouTube Terms of Service and local laws. The user is deemed to have accepted all legal responsibilities arising from the use of the software.

<p align="center">
<sub>Developed with ❤️ by Yusuf Can Ozan</sub>
</p>
