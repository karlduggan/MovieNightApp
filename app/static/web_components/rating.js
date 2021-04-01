// Enter the below in the html file to access the component
// <script src="{{ url_for('static', filename='folderName/rating.js') }}"></script>

window.customElements.define(
    'star-rating',
    class component extends HTMLElement {
      constructor() {
        super();
        const shadowRoot = this.attachShadow({mode: 'open'});
    
        shadowRoot.innerHTML = `
        <style>
        

        </style>
        <div class="stars" data-stars="1">
            <svg height="25" width="23" id="star-one">
            <polygon points="9.9, 1.1, 3.3, 21.78, 19.8, 8.58, 0, 8.58, 16.5, 21.78" style="fill-rule:nonzero;"/>
            </svg>

            <svg height="25" width="23" id="star-two" >
            <polygon points="9.9, 1.1, 3.3, 21.78, 19.8, 8.58, 0, 8.58, 16.5, 21.78" style="fill-rule:nonzero;"/>
            </svg>

            <svg height="25" width="23" id="star-three">
            <polygon points="9.9, 1.1, 3.3, 21.78, 19.8, 8.58, 0, 8.58, 16.5, 21.78" style="fill-rule:nonzero;"/>
            </svg>

            <svg height="25" width="23" id="star-four">
            <polygon points="9.9, 1.1, 3.3, 21.78, 19.8, 8.58, 0, 8.58, 16.5, 21.78" style="fill-rule:nonzero;"/>
            </svg>

            <svg height="25" width="23" id="star-five">
            <polygon points="9.9, 1.1, 3.3, 21.78, 19.8, 8.58, 0, 8.58, 16.5, 21.78" style="fill-rule:nonzero;"/>
            </svg>
        </div>
        `;
      }
      // SVG Star rating function gets a value between 0 10 and converts it
      // to a five star equivalent 
      setRating(rating) {
          let stars = ['star-one', 'star-two','star-three','star-four','star-five']
          let round_off_rating = Math.round(rating)
          console.log(round_off_rating)
          let star_rating = 0
          if(round_off_rating % 2 === 0){
              star_rating = round_off_rating / 2
          } else {
                star_rating = (round_off_rating - 1) / 2
          }
          // Iterate through the stars with the star rating value
          for(var i = 0; i < star_rating; i++){
            console.log(stars[i])
            this.shadowRoot.getElementById(stars[i]).setAttribute("fill", "yellow")
          }
          
          }
      connectedCallback() {
        this.setRating(this.getAttribute('rating'))
      }

    }
  );