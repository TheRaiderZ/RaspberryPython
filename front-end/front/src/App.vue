<template>
  <div>
    <h1 class="titre">MLAB</h1>
    <h2 class="">Votre lavage de main a duré {{this.temps.toFixed(2)}}s !</h2>
    <c-resultat :distance="distance" 
    :savon="savon"  
    :temps="temps" 
    :rotationG="rotationG" 
    :rotationD="rotationD"
    :tempsGauche="tempsGauche"
    :tempsDroit="tempsDroit"
    ></c-resultat>

  </div>
</template>

<script>
import CResultat from "./components/Resultat.vue";
// import dataJson from '../../../data.json';
export default {
  name: "App",
  components: {
    CResultat,
  },
  data() {
    return {
      result: null,
      
    };
  },
  computed: {
    savon() {
      return this.result.savon ?? 0;
    },
    temps() {
      return this.result.temps ?? 0;
    },
    distance() {
      return this.result.distance ?? 0;
    },
    rotationG() {
      return this.result.rotationG ?? 0;
    },
    rotationD() {
      return this.result.rotationD ?? 0;
    },
    tempsGauche() {
      return this.result.tempsGauche ?? 0;
    },
    tempsDroit() {
      return this.result.tempsDroit ?? 0;
    },

  },
  methods: {
    async getResultat() {
      import("../../../data.json").then(data=>this.result=data.data).then(()=>console.log(this.result));
     
      // fetch("http://127.0.0.1:5000/getData")
      //   .then((res) => {
      //     return res.json();
      //   })
      //   .then((data) => {
      //     this.result = data.data;
      //     console.log("data", this.result);
      //   })
      //   .catch((err) => {
      //     console.log({ err });
      //   });
    },
  },
  beforeMount() {
    this.getResultat();

    setInterval(() => {
      this.getResultat();
    }, 100000);
  },
};
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
