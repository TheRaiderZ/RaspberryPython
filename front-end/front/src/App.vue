<template>
  <div>
    <h1 class="titre">MLAB</h1>
    <c-resultat :distance="distance" 
    :savon="savon"  
    :temps="temps" 
    :rotationG="rotationG" 
    :rotationD= "rotationD"></c-resultat>

  </div>
</template>

<script>
import CResultat from "./components/Resultat.vue";

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
      return this.result.savon ?? 0.1;
    },
    temps() {
      return this.result.temps ?? 0.1;
    },
    distance() {
      return this.result.distance ?? 0.1;
    },
    rotationG() {
      return this.result.rotationG ?? 0.1;
    },
    rotationD() {
      return this.result.rotationD ?? 0.1;
    }

  },
  methods: {
    getResultat() {
      fetch("http://127.0.0.1:5000/getData")
        .then((res) => {
          return res.json();
        })
        .then((data) => {
          this.result = data.data;
          console.log("data", this.result);
        })
        .catch((err) => {
          console.log({ err });
        });
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
