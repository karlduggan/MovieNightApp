window.customElements.define(
    'movie-card',
    class MovieCard extends HTMLElement {
      constructor() {
        super();
        const shadowRoot = this.attachShadow({mode: 'open'});
        shadowRoot.innerHTML = `
        <div id='output2'></div>
        `;
      }
      connectedCallback() {
        this.firstChange();
      }
      firstChange(){
        const moviecard = this.shadowRoot.querySelector('moviecard')
        
        fetch('http://127.0.0.1:5000/api/v1/resources/movies?id=5')
            .then((res)=> res.json())
            .then((data)=> {
                let output = '';
                data.forEach(function(movie){
                    output += `
                    <div>
                        <h3>${movie.title}</h3>
                        <p>${movie.overview}</p>
                        <h4>${movie.year}</h4>
                        <p>${movie.runtime}</p>
                    </div>
                    `;
                });
                
            })
      }
    }
    
  );
