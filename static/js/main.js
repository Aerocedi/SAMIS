new Vue({
    el:'#app',
    delimiters:['[[',']]'],

    data:{
    name: 'Dashboard',
    dashboard:true,
    task:false,
    zewer:false,
    module:false,
    },

    methods: {
        changeTitle(title){
            return this.name=title
        },
        showHome:function(){
            
            this.dashboard=true
            this.task=false
            this.changeTitle("Dashboard")
        },
        assignTask:function(){
            this.dashboard=false,
            this.task=true,
            this.changeTitle("Task")
        },
        checkValue:function(){
            seleTask=document.getElementById('taskbreak').value;
            return seleTask
        },
        checkTask:function(){
            
           
            if (this.checkValue()=='New Engine Record'){
                this.zewer=true
            }

            if (checkValue()=='Module(s) Swapping'){
               this.module=true
            }
        },
        
    }
})