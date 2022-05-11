<template>
  <div class="container">
      <div class="oneline">
          <h2>Temps du lavage : </h2>
          <p>
              {{scoreEau}} / 10
          </p>
      </div>

      <div class="oneline">
          <h2>Quantité de savon utilisé :</h2>
          <p>
              {{scoreSavon}} / 10
          </p>
      </div>
  </div>
</template>

<script>
export default {
    name: 'MyResultat',
    computed:{
        scoreEau(){
            return this.eau
        },
        scoreSavon(){
            return this.savon
        }
    },
    props:{
        eau :{
            type: Number,
            required: true
        },
        savon:{
            type:Number,
            required : true
        }
    },
    methods:{
       
    },
    mounted(){
        // this.scoreEau = +this.eau;    
    },
    beforeMount(){
        // alert("hello")
    }
}
</script>

<style scoped>


.oneline{
    display: flex;
    align-items: center;
    justify-content: space-between;
}


.container{
    border: 1px none black;
    border-radius: 5px;
    width: 30%;
    margin : 0 auto; 
    padding: 1% 2%;
    background: rgba(173, 233, 235, 0.5);
    /* border: none; */
   
}

.container:hover{
    box-shadow: 2px 2px 15px 1px rgb(100, 219, 124);
}


</style>