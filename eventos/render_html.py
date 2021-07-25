
'http://127.0.0.1:8000/eventos/1/2021-07-29/'

text = '''
    {% load static %}
<!DOCTYPE html>
<html lang="en">
<html style="font-size: 16px;">



<body>
<button id="button">Download</button>
</body>
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/0.5.0-beta4/html2canvas.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/0.5.0-beta4/html2canvas.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/0.5.0-beta4/html2canvas.svg.js"></script> 
  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/0.5.0-beta4/html2canvas.svg.min.js"></script>  
</head>


  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">
    <meta name="keywords" content="">
    <meta name="description" content="">
    <meta name="page_type" content="np-template-header-footer-from-plugin">
    <title>Página Inicial</title>
    <link rel="stylesheet"  type=text/css href="{% static '/css/nicepage_evento.css' %}" media="screen">
    <link rel="stylesheet"  type=text/css href="{% static '/css/Página_evento.css' %}" media="screen">
    <script class="u-script" type="text/javascript" src="{% static '/js/jquery_evento.js' %}" defer=""></script>
    <script class="u-script" type="text/javascript" src="{% static '/js/nicepage_evento.js' %}" defer=""></script>
    <meta name="generator" content="Nicepage 3.15.3, nicepage.com">
    <link id="u-theme-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i">
    
    
    <script type="application/ld+json">{
		"@context": "http://schema.org",
		"@type": "Organization",
		"name": "",
		"url": "Pagina_evento.html",
		"logo": "images/default-logo.png"
}</script>
    <meta property="og:title" content="Página Inicial">
    <meta property="og:type" content="website">
    <meta name="theme-color" content="#478ac9">
    <link rel="canonical" href="Pagina_evento.html">
    <meta property="og:url" content="Pagina_evento.html">
  </head>
  <body data-home-page="Página_evento.html" data-home-page-title="Página evento" class="u-body"><header class="u-clearfix u-header u-header" id="main"><div class="u-clearfix u-sheet u-valign-middle u-sheet-1">
        <a href="https://nicepage.com" class="u-image u-logo u-image-1">
          <img src="{% static 'images/default-logo.png' %}" class="u-logo-image u-logo-image-1">
        </a>
        <nav class="u-menu u-menu-dropdown u-offcanvas u-menu-1">
          <div class="menu-collapse" style="font-size: 1rem; letter-spacing: 0px;">
            <a class="u-button-style u-custom-left-right-menu-spacing u-custom-padding-bottom u-custom-top-bottom-menu-spacing u-nav-link u-text-active-palette-1-base u-text-hover-palette-2-base" href="#">
              <svg><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#menu-hamburger"></use></svg>
              <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><symbol id="menu-hamburger" viewBox="0 0 16 16" style="width: 16px; height: 16px;"><rect y="1" width="16" height="2"></rect><rect y="7" width="16" height="2"></rect><rect y="13" width="16" height="2"></rect>
</symbol>
</defs></svg>
            </a>
          </div>
          <div class="u-nav-container">
            <ul class="u-nav u-unstyled u-nav-1"><li class="u-nav-item"><a class="u-button-style u-nav-link u-text-active-palette-1-base u-text-hover-palette-2-base" href="Página-Inicial.html" style="padding: 10px 20px;">Página Inicial</a>
       {% for i in eventos %}     
</li><li class="u-nav-item"><a class="u-button-style u-nav-link u-text-active-palette-1-base u-text-hover-palette-2-base" href="Sobre.html" style="padding: 10px 20px;">{{i.descricao_evento}}</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link u-text-active-palette-1-base u-text-hover-palette-2-base" href="Contact.html" style="padding: 10px 20px;">{{i.data_evento}}</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link u-text-active-palette-1-base u-text-hover-palette-2-base" href="Página-1.html" style="padding: 10px 20px;">Página 1</a>
</li></ul>
        {% endfor %}
          </div>
          <div class="u-nav-container-collapse">
            <div class="u-black u-container-style u-inner-container-layout u-opacity u-opacity-95 u-sidenav">
              <div class="u-sidenav-overflow">
                <div class="u-menu-close"></div>
                <ul class="u-align-center u-nav u-popupmenu-items u-unstyled u-nav-2"><li class="u-nav-item"><a class="u-button-style u-nav-link" href="Página-Inicial.html">Página Inicial</a>

</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="Sobre.html">Sobre</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="Contact.html">{{eventos.titulo_evento}}</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="Página-1.html">{{eventos.titulo_evento}}</a>
</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="Página-1.html">Galeria do evento</a>
</li></ul>
              </div>
            </div>
            <div class="u-black u-menu-overlay u-opacity u-opacity-70"></div>
          </div>
        </nav>
      </div></header>
    <section class="u-align-center u-clearfix u-section-1" id="sec-b7bd">
      <div class="u-clearfix u-sheet u-sheet-1">
        <ul> 
        </ul>
        {% for i in imagens %}
        <div class="u-expanded-width u-gallery u-layout-horizontal u-lightbox u-no-transition u-show-text-on-hover u-gallery-1">
          <div class="u-gallery-inner"><div class="u-effect-fade u-gallery-item u-gallery-item-1"><div class="u-back-slide"><img class="u-back-image" src="{{i.images.url}}">
</div>
{% endfor %}

</div></div>
          <a class="u-absolute-vcenter u-gallery-nav u-gallery-nav-prev u-grey-70 u-icon-circle u-opacity u-opacity-70 u-spacing-10 u-text-white u-gallery-nav-1" href="#" role="button">
            <span aria-hidden="true">
              <svg viewBox="0 0 451.847 451.847"><path d="M97.141,225.92c0-8.095,3.091-16.192,9.259-22.366L300.689,9.27c12.359-12.359,32.397-12.359,44.751,0
c12.354,12.354,12.354,32.388,0,44.748L173.525,225.92l171.903,171.909c12.354,12.354,12.354,32.391,0,44.744
c-12.354,12.365-32.386,12.365-44.745,0l-194.29-194.281C100.226,242.115,97.141,234.018,97.141,225.92z"></path></svg>
            </span>
            <span class="sr-only">
              <svg viewBox="0 0 451.847 451.847"><path d="M97.141,225.92c0-8.095,3.091-16.192,9.259-22.366L300.689,9.27c12.359-12.359,32.397-12.359,44.751,0
c12.354,12.354,12.354,32.388,0,44.748L173.525,225.92l171.903,171.909c12.354,12.354,12.354,32.391,0,44.744
c-12.354,12.365-32.386,12.365-44.745,0l-194.29-194.281C100.226,242.115,97.141,234.018,97.141,225.92z"></path></svg>
            </span>
          </a>
          <a class="u-absolute-vcenter u-gallery-nav u-gallery-nav-next u-grey-70 u-icon-circle u-opacity u-opacity-70 u-spacing-10 u-text-white u-gallery-nav-2" href="#" role="button">
            <span aria-hidden="true">
              <svg viewBox="0 0 451.846 451.847"><path d="M345.441,248.292L151.154,442.573c-12.359,12.365-32.397,12.365-44.75,0c-12.354-12.354-12.354-32.391,0-44.744
L278.318,225.92L106.409,54.017c-12.354-12.359-12.354-32.394,0-44.748c12.354-12.359,32.391-12.359,44.75,0l194.287,194.284
c6.177,6.18,9.262,14.271,9.262,22.366C354.708,234.018,351.617,242.115,345.441,248.292z"></path></svg>
            </span>
            <span class="sr-only">
              <svg viewBox="0 0 451.846 451.847"><path d="M345.441,248.292L151.154,442.573c-12.359,12.365-32.397,12.365-44.75,0c-12.354-12.354-12.354-32.391,0-44.744
L278.318,225.92L106.409,54.017c-12.354-12.359-12.354-32.394,0-44.748c12.354-12.359,32.391-12.359,44.75,0l194.287,194.284
c6.177,6.18,9.262,14.271,9.262,22.366C354.708,234.018,351.617,242.115,345.441,248.292z"></path></svg>
            </span>
          </a>
        </div>
        <h6 class="u-text u-text-1">Artistas<br>
        </h6>
        <h6 class="u-text u-text-2">{{evento.titulo_evento}}</h6>
        <h6 class="u-text u-text-3">{{evento.data_evento}}</h6>
        <h3 class="u-text u-text-4">Titulo Evento</h3>
        <h5 class="u-text u-text-5"></h5>
      </div>
    </section>
   
    <footer class="u-align-center u-clearfix u-footer u-grey-80 u-footer" id="sec-77f5"><div class="u-clearfix u-sheet u-sheet-1">
        <p class="u-small-text u-text u-text-variant u-text-1">Amostra de texto. Lorem ipsum dolor sit amet, consectetur adipiscing elit nullam nunc justo sagittis suscipit ultrices.</p>
      </div></footer>
    <section class="u-backlink u-clearfix u-grey-80">
      <a class="u-link" href="https://nicepage.com/website-templates" target="_blank">
        <span>Website Templates</span>
      </a>
      <p class="u-text">
        <span>created with</span>
      </p>
      <a class="u-link" href="https://nicepage.com/" target="_blank">
        <span>Website Builder Software</span>
      </a>. 
    </section>
  </body>
 

</html>
</html>
<button id="button" onclick="saveCanvas()" >Download</button>
<script>



 function saveCanvas(){

  var str= String(window.location.href)
    
      var id= str[str.length- 2];
      var splits = str.split(/([0-9]+)/);
      var id = splits[13] + splits[14] + splits[15] + splits[16] + splits[17]
      //var id = splits[3] + splits[4] + splits[5] + splits[6] + splits[7] // se estiver a correr em heroku
      console.log(splits)
      console.log(id)

    html2canvas(document.querySelector("#sec-77f5")).then(canvas => {
      var image = canvas.toDataURL("image/png");
      saveAs(canvas.toDataURL(), 'evento-canvas'+id);
      
  

    });
  }  

  function saveAs(uri, filename) {
        var link = document.createElement('a');
        if (typeof link.download === 'string') {
          link.href = uri;
          link.download = filename;

          //Firefox requires the link to be in the body
          document.body.appendChild(link);

          //simulate click
          link.click();

          //remove the link when done
          document.body.removeChild(link);
        } else {
          window.open(uri);
        }
      }
</script>


    '''


file = open("123.html","w")

file.write(text)

file.close()