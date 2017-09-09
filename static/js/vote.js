var newWidth,
    mouth = $("#mouth");

$( "#slider" ).slider({
   slide: function(event, ui) {
     $("#vote").val( ui.value )

     if (ui.value > 51 ) {
       
       mouth.css({ bottom: 0, top: "auto" });
       
       newWidth = 160 - ui.value;
       
       mouth.css({
         width           : newWidth,
         height          : newWidth,
         "border-radius" : newWidth / 2,
         left            : -25 + ((ui.value-50) / 2)
       })
       .removeClass("straight");
       
     } else if ((ui.value > 48) && (ui.value < 52)) {
       
       mouth.addClass("straight");
       
     }  else {
       
       mouth.css({ top: 0, bottom: "auto" });
       
       newWidth = ui.value + 60;
       
       mouth.css({
         width           : newWidth,
         height          : newWidth,
         "border-radius" : newWidth / 2,
         left            : -ui.value / 2
       })
       .removeClass("straight");
       
     }
     
   },
  value: 50
});