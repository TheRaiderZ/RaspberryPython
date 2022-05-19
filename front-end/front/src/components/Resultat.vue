<template>
  <div class="container">
      <!-- <div class="oneline">
          <h2>Distance de l'évier : </h2>
          <p>
              {{distance}}
          </p>
      </div> -->
        <div class="oneline">
            <h2>Vos temps :</h2>
            <p>
                <span>Gauche : </span>
                {{tempsGauche.toFixed(2)}}s
            </p>
            <p>
                <span>Droit : </span>
                {{tempsDroit.toFixed(2)}}s
            </p>
        </div>
      <div class="oneline">
          <h2>Quantité de savon :</h2>
          <p>
              {{scoreSavon[0]}} / 2
          </p>
          
          <em>{{scoreSavon[1]}}</em>
      </div>

        <div class="oneline">
            <h2>Temps :</h2>
            <p>
                {{scoreTemps[0]}} / 2
            </p>
            
            <em>{{scoreTemps[1]}}</em>
        </div>
        
        <div class="oneline">
            <h2>Robinet gauche :</h2>
            <p>
                {{scoreTempsGauche[0]}} /2
            </p>
            
            <em>{{scoreTempsGauche[1]}}</em>
        </div>

        <div class="oneline">
            <h2>Robinet Droit :</h2>
            <p>
                {{scoreTempsDroit[0]}} /2
            </p>
            <em>{{scoreTempsDroit[1]}}</em>
        </div>


      
  </div>
</template>

<script>
export default {
    name: 'MyResultat',
    computed:{
        scoreDistance(){
            return this.distance
        },
        scoreSavon(){
            var messageSavon='';
            if (this.savon<=0){
                messageSavon="Pas de savon !"; 
                return [0, messageSavon];
            }
            else if (this.savon>0 && this.savon<=3){
                messageSavon="Quantité idéale !";
                return [2, messageSavon];
            }
            else {
                messageSavon="Trop de savon !";
                return [1, messageSavon]; //Trop de savon
            }
                
        },
        scoreTemps(){
            var messageTemps='';
            if (this.temps<=0){
                messageTemps="Pas lavé !";
                return [0, messageTemps]; //Pas de temps
            }
            else if (this.temps>0 && this.temps<30){
                messageTemps=`Temps trop court ! (- de 30s)`;
                return [1, messageTemps]; //Temps trop court
            }
            else if (this.temps>=30 && this.temps<=60){
                messageTemps=`Temps juste ! (>= 30s et <= 60s)`;
                return [2, messageTemps]; //Temps idéal
            }
            else {
                messageTemps=`Trop long, gaspillage d'eau ! (> 60s)`;
                return [1, messageTemps]; //Trop long
            }
            // return this.temps
        },
        scoreTempsGauche(){
            var messageTempsGauche='';
            if (this.tempsGauche<=0){
                messageTempsGauche="Pas lavé !";
                return [0, messageTempsGauche]; //Pas de temps
            }
            else if (this.tempsGauche>0 && this.tempsGauche<30){
                messageTempsGauche=`Temps trop court ! (- de 30s)`;
                return [1, messageTempsGauche]; //Temps trop court
            }
            else if (this.tempsGauche>=30 && this.tempsGauche<=60){
                messageTempsGauche=`Temps juste ! (>= 30s et <= 60s)`;
                return [2, messageTempsGauche]; //Temps idéal
            }
            else {
                messageTempsGauche=`Trop long, gaspillage d'eau ! (> 60s)`;
                return [1, messageTempsGauche]; //Trop long
            }
                
            // return this.tempsGauche
        },
        scoreTempsDroit(){
            var messageTempsDroit='';
            if (this.tempsDroit<=0){
                messageTempsDroit="Pas lavé !";
                return [0, messageTempsDroit]; //Pas de temps
            }
            else if (this.tempsDroit>0 && this.tempsDroit<30){
                messageTempsDroit=`Temps trop court ! (- de 30s)`;
                return [1, messageTempsDroit]; //Temps trop court
            }
            else if (this.tempsDroit>=30 && this.tempsDroit<=60){
                messageTempsDroit=`Temps juste ! (>= 30s et <= 60s)`;
                return [2, messageTempsDroit]; //Temps idéal
            }
            else {
                messageTempsDroit=`Trop long, gaspillage d'eau ! (> 60s)`;
                return [1, messageTempsDroit]; //Trop long
            }
            // return this.tempsDroit
        }
    },
    props:{
        distance :{
            type: Number,
            required: true
        },
        savon:{
            type:Number,
            required : true
        },
        temps:{
            type:Number,
            required: true
        },
        tempsGauche:{
            type:Number,
            required: true
        },
        tempsDroit:{
            type:Number,
            required: true
        },
    },
    data(){
        return {
            
        };
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