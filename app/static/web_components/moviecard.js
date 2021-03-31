window.customElements.define(
  'movie-card',
  class component extends HTMLElement {
    constructor() {
      super();
      const shadowRoot = this.attachShadow({mode: 'open'});
  
      shadowRoot.innerHTML = `
      <style>
      @import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400,700);
      a {
        text-decoration: none;
        color: rgb(230, 230, 230);
     }
      h1 {
        font-family: 'Open Sans', sans-serif;
        font-weight: 300;
     }
  
      .formFront {
        position: absolute;
        transform-style: preserve-3d;
        height: 520px;
        text-align: center;
        z-index: 900;
        -webkit-transform: rotateX(0deg) rotateY(0deg);
        -moz-transform: rotateX(0deg) rotateY(0deg);
        -o-transform: rotateX(0deg) rotateY(0deg);
        transform: rotateX(0deg) rotateY(0deg);
        -webkit-transition: all .6s ease-in-out;
        -moz-transition: all .6s ease-in-out;
        -o-transition: all .6s ease-in-out;
        transition: all .6s ease-in-out;
        -webkit-transform-style: preserve-3d;
        -moz-transform-style: preserve-3d;
        -o-transform-style: preserve-3d;
        transform-style: preserve-3d;
        -webkit-backface-visibility: hidden;
        -moz-backface-visibility: hidden;
        -o-backface-visibility: hidden;
        backface-visibility: hidden;
      }
      
      .formFront img {
        height: 100%;
        width:100%;
        background-size: auto;
        background-color: rgb(30, 40, 50);
        border-radius: 5px;
        box-shadow: 0 19px 38px rgba(0, 0, 0, 0.3), 0 15px 12px rgba(0, 0, 0, 0.2);
      }

    #formCard {
      margin: 5px;
      z-index: 1;
      transform-style: preserve-3d;
      display: inline-block;
    }

    #formCard.flip .formFront {
      z-index: 900;
      transform: rotateY(180deg);
    }
    
    .formBack {
      display: block;
      border-radius: 5px;
      z-index: 800;
      width: 350px;
      height: 520px;
      box-sizing: border-box;
      padding: 10px;
      color: rgba(255, 0, 0, 0.5);
      transform: rotateY(-180deg);
      transition: all .5s ease-in-out;
      transform-style: preserve-3d;
      backface-visibility: hidden;
      box-shadow: 0 19px 38px rgba(0, 0, 0, 0.3), 0 15px 12px rgba(0, 0, 0, 0.2);
    }

    .formBack .data .content {
      font-family: 'Open Sans', sans-serif;
      font-weight: 300;
      padding: 1em;
      z-index: 1;
      color: #fff9;
   }
    .formBack .year {
      font-size: 12px;
   }
    .formBack .title {
      margin-top: 10px;
      font-family: 'Open Sans', sans-serif;
      font-weight: 300;
      color: rgb(230, 230, 230);
   }
    .formBack .text {
      height: 70px;
      padding-top: 15px;
   }
   .formBack .overview {
    font-family: 'Open Sans', sans-serif;
    font-weight: 300;
    color: rgb(230, 230, 230);
   }
   .formBack .runtime {
    font-family: 'Open Sans', sans-serif;
    font-weight: 300;
    color: rgb(230, 230, 230);
   }
    
    #formCard.flip .formBack{
      color: #fff;
      background-color: rgb(30, 40, 50);
      z-index: 1000;
      transform: rotateY(0deg);
    }
      </style>


    <section id="formCard">
      <div class="formFront">
        <img src=${this.getAttribute('poster')}  width="350" >
      </div>

      <div class="formBack">
        <div class="data">
            <div class="content">
              
              <h1 class="title"><a href="#">${this.getAttribute('title')}</a></h1>
              <span class="year">${this.getAttribute('year')}</span>
              <p class="overview">Overview</p>
              <p class="text">${this.getAttribute('overview')}</p>
              <p class="runtime">Runtime</p>
              <p>${this.getAttribute('runtime')}</p>
            </div>
         
        </div>
      </div>
    </section>   
 
      `;
    }

    flip_card(){
      this.shadowRoot.getElementById("formCard").classList.toggle("flip");
    };
    connectedCallback() {
      this.shadowRoot.querySelector(".formFront").addEventListener('click', () => this.flip_card())
      this.shadowRoot.querySelector(".formBack").addEventListener('click', () => this.flip_card())
    }   
  }
);
