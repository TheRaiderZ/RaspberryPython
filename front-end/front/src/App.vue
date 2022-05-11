<template>
  <div>
    <h1 class="titre">MLAB</h1>
    <resultat eau="0" savon="7"></resultat>
  </div>
</template>

<script>
import Resultat from "./components/Resultat.vue";
// import axios from "axios";

export default {
  name: "App",
  components: {
    Resultat,
  },
  data(){
    return{
      resultat: null,
    }
  },
  methods:{
    getResultat(){
       fetch("http://127.0.0.1:5000/getData")
    // axios
      // .get("https://localhost:5000/getData")
      .then(res => {
        console.log(res)
      })
      .catch(err=>{
        console.log({err})
      })
    },
  },

  created(){
    this.getResultat();

    setInterval(() => {
      this.getResultat();
    }, 10000);
  },
  beforeMount() {

   
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

* {
  box-sizing: border-box;
}

body {
  background: rgb(240, 207, 122);
}

.titre {
  color: red;
  font-size: 3rem;
}
</style>
