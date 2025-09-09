# Movie Info GUI
A modern Python desktop application that allows users to search for movies, view detailed information, 
and manage favorite/watch lists using the **[OMDb API](https://www.omdbapi.com/)**. Built with **CustomTkinter** for a clean, responsive, 
and user-friendly interface.

---

## Table of Contents  

- [English Section](#movie-info-gui)  
- [Türkçe Bölüm](#movie-info-gui-tr)  

---

## Contents

- [Overview](#overview)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [File Structure](#file-structure)  
- [License](#license)  
- [Author](#author)  

---

## Overview

Movie Info GUI is a modern Python desktop application built with **CustomTkinter** that allows users to 
search for movies and view detailed information fetched from the **OMDb API**. The interface is clean, 
intuitive, and visually appealing, offering a superior experience compared to traditional CLI-based movie info tools.


---

## Features

### Current Features
- **Movie Search:**  
  - Search for any movie by title. A default movie (“Interstellar”) is displayed on startup.  


- **Movie Details:**  
  - Displays: Title, Year, Type, Genre, Runtime, IMDb Rating, Director, Actors, Language, Country, Awards, and Plot.  


- **Poster Display:**  
  - Shows movie poster in a framed area.  
  - Clickable poster opens IMDb page in browser.  
  - Hover effect: cursor changes on poster hover.  
  - Handles missing posters gracefully. 


- **Favorites & Watch Lists:**  
  - Add movies to **Favorites** or **To Watch** lists.  
  - Saved locally in JSON with timestamp.  
  - Duplicate entries prevented.  
  - Lists are read-only in GUI.  


- **GUI Design:**  
  - Dark-themed modern interface using CustomTkinter.  
  - Clear fonts and button colors for readability.  
  - Panels for Search, Movie Details, and Favorites/Watch lists.  
  - Default focus on search entry for faster interaction.  


- **Error Handling:**  
  - Handles API errors, timeouts, and missing data.  
  - Shows messages when movies are not found or poster fails to load.  


- **Data Management:**  
  - Structured utils module for saving/loading lists.  
  - Automatically creates JSON files if missing.  
  - Avoids crashes due to empty or malformed JSON files. 

### Planned Features
- **Theme Switching:**
   - Switch between Dark and Light modes for better user experience.
   - Additional color themes can be selected to customize the interface.

---

## Installation

Follow these steps to set up **Movie Info GUI** on your system.

### 1. Clone the repository  
   Open a terminal or command prompt and run:
```bash
  git clone https://github.com/berkdnmz/movie-info-gui.git  
  cd movie-info-gui  
```
### 2. Create a virtual environment  
   It is recommended to use a virtual environment to avoid conflicts with other Python packages.
```bash
  python -m venv .venv
```
### 3. Activate the virtual environment

- **Windows (PowerShell):**
```powershell
  .venv\Scripts\Activate.ps1
```
- **Windows (Command Prompt):**
```cmd
  .venv\Scripts\activate.bat
```
- **Linux / macOS:**
```bash
  source .venv/bin/activate
```
   After activation, your terminal should indicate that the virtual environment is active (usually `(.venv)` appears in the prompt).

### 4. Install dependencies

   Install the required Python packages:
```bash
  pip install -r requirements.txt
```

### 5. Set your OMDb API key
   Create a `.env` file in the project root and add your **API key:**
```bash
  # Linux/macOS
  echo "API_KEY=your_api_key_here" > .env
   
  # Windows (PowerShell)
  echo "API_KEY=your_api_key_here" > .env
   
  # Windows (CMD)
  echo API_KEY=your_api_key_here > .env
```
You can get a free OMDb API key from **[OMDb API](http://www.omdbapi.com/apikey.aspx)**

### 6. Run the application
   Make sure your virtual environment is active, then run:
```bash
  python -m src.main
```
The application should launch, displaying the default movie `(Interstellar)` on startup.

---

## Usage

After completing the installation steps, you can run the application:

```bash
  python -m src.main
```
### 1. Search for Movies  

  - Type the name of a movie in the search bar at the top.
  - Press Enter or click the search button to fetch movie details.

### 2. View Movie Details 

  - The app will display comprehensive information including:  

    - Title, Year, Type, Genre
    - Runtime
    - IMDb Rating
    - Director and Actors
    - Language and Country
    - Awards
    - Plot (Synopsis)
  -  The movie poster is displayed in the left panel.

### 3. Interact with Poster

  - Click on the poster to open the IMDb page for the movie.
  - Hovering over the poster changes the cursor to indicate interactivity.

### 4. Manage Lists

  - Use **Add to Favorites** to save the movie to your favorites list.
  - Use **Add to Watch** to save the movie to your “To Watch” list.
  - Duplicate movies cannot be added.
  - Lists are saved locally in JSON files and are read-only in the GUI.

### 5. Exit the Application

  - Press **Escape (Esc)** at any time to close the application.
---
## File Structure
```text
movie-info-gui/
│
├─ src/                         # Source code
│  ├─ __init__.py               # Makes src a package
│  ├─ gui/                      # GUI components
│  │  ├─ __init__.py            # Makes gui a package
│  │  ├─ search_panel.py        # Search panel UI
│  │  ├─ movie_detail_panel.py  # Movie detail panel UI
│  │  └─ favorites_panel.py     # Favorites and To Watch panel UI
│  ├─ api_handler.py            # Handles OMDb API requests
│  ├─ utils.py                  # Utility functions (save/load, clean_value, etc.)
│  └─ main.py                   # Application entry point
│
├─ data/                        # JSON files storing user lists
│  ├─ favorites.json            # Favorite movies
│  └─ to_watch.json             # Movies to watch
│
├─ .env                         # Environment file for API key
├─ requirements.txt             # Python dependencies
├─ LICENSE                      # Project license
└─ README.md                    # Project documentation
```
---

## License

This project is open source under the [MIT License](LICENSE).  

---

## Author

**Berk Dönmez**  

- GitHub: [github.com/berkdnmz](https://github.com/berkdnmz)  
- LinkedIn: [linkedin.com/in/berkdnmz](https://linkedin.com/in/berkdnmz)

You can contact me for any questions or suggestions regarding the project.

***Happy coding and enjoy exploring movies with Movie Info GUI!***


---

# Movie Info GUI [TR]

Kullanıcıların filmleri arayabileceği, detaylı bilgilerini görüntüleyebileceği ve **OMDb API** 
kullanarak favori/izleme listelerini yönetebileceği modern bir Python masaüstü uygulamasıdır. 
Arayüz, **CustomTkinter** ile geliştirilmiş olup, temiz, duyarlı ve kullanıcı dostu bir deneyim sunar.

---

## İçindekiler

- [Genel Bakış](#genel-bakış)  
- [Özellikler](#özellikler)  
- [Kurulum](#kurulum)  
- [Kullanım](#kullanım)  
- [Dosya Yapısı](#dosya-yapısı)  
- [Lisans](#lisans)  
- [Yazar](#yazar)  

---

## Genel Bakış

Movie Info GUI, kullanıcıların filmleri aramasına ve **[OMDb API](https://www.omdbapi.com/)** üzerinden çekilen detaylı bilgileri görüntülemesine olanak tanıyan, 
**CustomTkinter** ile geliştirilmiş modern bir Python masaüstü uygulamasıdır. Arayüzü temiz, sezgisel ve görsel olarak çekici olup, 
geleneksel komut satırı tabanlı film bilgi araçlarına kıyasla üstün bir deneyim sunar. 

---

## Özellikler

### Mevcut Özellikler
- **Film Arama:**  
  - Herhangi bir filmi başlığa göre arayın. Başlangıçta varsayılan bir film (“Interstellar”) gösterilir.  


- **Film Detayları:**  
  - Gösterilen bilgiler: Başlık, Yıl, Tür, Türler, Süre, IMDb Puanı, Yönetmen, Oyuncular, Dil, Ülke, Ödüller ve Konu.  


- **Poster Gösterimi:**  
  - Film posteri çerçeveli bir alanda gösterilir.  
  - Postere tıklayınca IMDb sayfası tarayıcıda açılır.  
  - Üzerine gelindiğinde imleç değişir (hover efekti).  
  - Poster yoksa uygun şekilde yedek gösterim yapılır.  


- **Favoriler & İzleme Listeleri:**  
  - Filmleri **Favoriler** veya **İzlenecekler** listesine ekleyin.  
  - JSON dosyalarında yerel olarak ve zaman damgasıyla kaydedilir.  
  - Aynı film birden fazla kez eklenemez.  
  - Listeler GUI’de sadece okunabilir.  


- **GUI Tasarımı:**  
  - **CustomTkinter** ile modern ve koyu tema arayüz.  
  - Okunabilirlik için net yazı tipleri ve buton renkleri.  
  - Arayüz panelleri: Arama, Film Detayları ve Favoriler/İzleme Listesi.  
  - Varsayılan odak, hızlı etkileşim için arama kutusunda.  


- **Hata Yönetimi:**  
  - API hataları, zaman aşımı ve eksik veriler yönetilir.  
  - Film bulunamadığında veya poster yüklenemezse bilgilendirici mesajlar gösterilir.  


- **Veri Yönetimi:**  
  - Listeleri kaydetmek/yüklemek için yapılandırılmış utils modülü.  
  - Eksik JSON dosyaları otomatik oluşturulur.  
  - Boş veya bozuk JSON dosyalarından kaynaklı çökme engellenir.  

### Planlanan Özellikler
- **Tema Seçimi:**  
  - Koyu ve Açık modlar arasında geçiş yapılabilir.  
  - Arayüzü özelleştirmek için ek renk temaları seçilebilir.

---

## Kurulum

Aşağıdaki adımları izleyerek **Movie Info GUI** uygulamasını sisteminize kurabilirsiniz.

### 1. Depoyu klonlayın  

Terminal veya komut istemcisini açın ve çalıştırın:
```bash
  git clone https://github.com/berkdnmz/movie-info-gui.git
  cd movie-info-gui
```

### 2. Sanal ortam oluşturun 
Diğer Python paketleriyle çakışmaları önlemek için sanal ortam kullanmanız önerilir.
```bash
  python -m venv .venv
```
### 3. Sanal ortamı etkinleştirin

- **Windows (PowerShell):**
```powershell
  .venv\Scripts\Activate.ps1
```
- **Windows (Komut İstemi / CMD):**
```cmd
  .venv\Scripts\activate.bat
```
- **Linux / macOS:**
```bash
  source .venv/bin/activate
```
Terminalde sanal ortamın aktif olduğunu gösteren bir işaret görmelisiniz **genellikle `(.venv)`**.

### 4. Gerekli paketleri yükleyin
```bash
  pip install -r requirements.txt  
```

### 5. OMDb API anahtarınızı ayarlayın
Proje kök dizininde `.env` dosyası oluşturun ve API anahtarınızı ekleyin:
```bash
  # Linux/macOS
  echo "API_KEY=api_anahtarınız_buraya" > .env
   
  # Windows (PowerShell)
  echo "API_KEY=api_anahtarınız_buraya" > .env
   
  # Windows (CMD)
  echo API_KEY=api_anahtarınız_buraya > .env
```
Ücretsiz bir OMDb API anahtarı almak için **[OMDb API](http://www.omdbapi.com/apikey.aspx)** sitesini ziyaret edebilirsiniz.

### 6. Uygulamayı çalıştırın
Sanal ortamın aktif olduğundan emin olduktan sonra:
```bash
  python -m src.main  
```
Uygulama açılacak ve başlangıçta varsayılan film `(Interstellar)` gösterilecektir.

---

## Kullanım
Kurulum adımlarını tamamladıktan sonra uygulamayı çalıştırabilirsiniz:
```bash
  python -m src.main  
```
### 1. Film Arama
- Üstteki arama çubuğuna bir film adı yazın.
- Enter tuşuna basın veya arama butonuna tıklayın, film detayları getirilecektir.

### 2. Film Detaylarını Görüntüleme
- Uygulama aşağıdaki bilgileri kapsamlı şekilde gösterir:
    - Başlık, Yıl, Tür, Tür (Film/Dizi vb.)
    - Süre
    - IMDb Puanı
    - Yönetmen ve Oyuncular
    - Dil ve Ülke
    - Ödüller
    - Konu (Özet)
-  Film posteri sol panelde görüntülenir.

### 3. Poster ile Etkileşim
- Postere tıklayarak filmin IMDb sayfasını açabilirsiniz
- Poster üzerine geldiğinizde imleç değişerek etkileşimi gösterir.

### 4. Listeleri Yönetme
- **Favorilere Ekle** butonu ile filmi favori listenize kaydedin.
- **İzlenecekler Listesine Ekle** butonu ile filmi “İzlenecekler” listesine kaydedin.
- Aynı film birden fazla kez eklenemez.
- Listeler yerel olarak JSON dosyalarında saklanır ve arayüzden yalnızca okunabilir.

### 5. Uygulamadan Çıkış
- İstediğiniz zaman **Escape (Esc)** tuşuna basarak uygulamayı kapatabilirsiniz.

---

## Dosya Yapısı

```text
movie-info-gui/
│
├─ src/                         # Kaynak kodlar
│  ├─ __init__.py               # src klasörünü paket yapar
│  ├─ gui/                      # Arayüz bileşenleri
│  │  ├─ __init__.py            # gui klasörünü paket yapar
│  │  ├─ search_panel.py        # Arama paneli arayüzü
│  │  ├─ movie_detail_panel.py  # Film detay paneli arayüzü
│  │  └─ favorites_panel.py     # Favoriler ve İzlenecekler paneli arayüzü
│  ├─ api_handler.py            # OMDb API isteklerini yönetir
│  ├─ utils.py                  # Yardımcı fonksiyonlar (kaydet/yükle, clean_value vb.)
│  └─ main.py                   # Uygulamanın giriş noktası
│
├─ data/                        # Kullanıcı listelerini tutan JSON dosyaları
│  ├─ favorites.json            # Favori filmler
│  └─ to_watch.json             # İzlenecek filmler
│
├─ .env                         # API anahtarının bulunduğu ortam dosyası
├─ requirements.txt             # Python bağımlılıkları
├─ LICENSE                      # Proje lisansı
└─ README.md                    # Proje dokümantasyonu
```
---

## Lisans

Bu proje [MIT Lisansı](LICENSE) kapsamında açık kaynak olarak sunulmuştur.  

---

## Yazar

**Berk Dönmez**  
- GitHub: [github.com/berkdnmz](https://github.com/berkdnmz)  
- LinkedIn: [linkedin.com/in/berkdnmz](https://linkedin.com/in/berkdnmz)  

Herhangi bir soru veya öneriniz için benimle iletişime geçebilirsiniz.  

***İyi kodlamalar ve Movie Info GUI ile filmleri keşfetmenin tadını çıkarın!***
