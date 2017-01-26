    
    // SWIPING INTERACTION CODE
    
         function openNav() {
            document.getElementById("Filters").style.width = "auto";
            };
        
            var swipearea = document.getElementById('swipearea');
            var swipeareared = document.getElementById('swipeareared');
            var swipegesture = document.getElementById('swipegesture');
            var swipegesturered = document.getElementById('swipegesturered');
            var bodything = document.getElementById('bodything');
            var filterPanel = document.getElementById('filterPanel');
            var cardcontainer = document.getElementById('Container');
            var navbar = document.getElementById('navbar');
           /* var responsivecontainer = document.getElementById('responsivecontainer');*/

            var mc = new Hammer(filterPanel);
            var mc2 = new Hammer(bodything);
            var mc3 = new Hammer (swipearea);
            var mc4 = new Hammer (swipeareared);


            mc3.on("swiperight", function(ev) {


                filterPanel.style.webkitTransform ="translateX(0)";
                /*filters.style.webkitTransition = "width 300ms cubic-bezier(.10, .10, .25, .90)";*/
                filterPanel.style.webkitTransition = "width 300ms ease";
                filterPanel.style.width = "100%";
                cardcontainer.style.visibility = "hidden";

                navbar.style.background = "#FF626D"
                swipegesture.style.display = "none";
                bodything.style.maxWidth = "100%";

            });

            mc2.on("swiperight", function(ev) {
                   filterPanel.style.webkitTransform ="translateX(0)";
               /* filters.style.webkitTransition = "width 300ms cubic-bezier(.10, .10, .25, .90)";*/
                filterPanel.style.webkitTransition = "width 300ms ease";
                filterPanel.style.width = "100%";
                navbar.style.background = "#FF626D"
               cardcontainer.style.visibility = "hidden";

                swipegesture.style.display = "none";
                bodything.style.maxWidth = "100%";

            });

            mc.on("swipeleft", function(ev) {
                /*filters.style.transitionProperty = "width";
                filters.style.transitionDuration = "0.5s";*/
                filterPanel.style.width = "0";
                cardcontainer.style.visibility = "visible";
                swipegesturered.style.display = "none";
                swipeareared.style.height = "auto";
                navbar.style.background = "-webkit-linear-gradient(to right, #FF626D , #FFC371)" 
                navbar.style.background = "linear-gradient(to right, #FF626D , #FFC371)" 

                bodything.style.maxWidth = "380px";
            });

           mc4.on("swipeleft", function(ev) {
                /*filters.style.transitionProperty = "width";*
                filters.style.transitionDuration = "0.5s";*/
                navbar.style.background = "-webkit-linear-gradient(to right, #FF626D , #FFC371);" 
                navbar.style.background = "linear-gradient(to right, #FF626D , #FFC371);" 
                filterPanel.style.width = "0";
                cardcontainer.style.visibility = "visible";
                swipegesturered.style.display = "none";
                swipeareared.style.height = "auto";
               bodything.style.maxWidth = "380px";

            });


    