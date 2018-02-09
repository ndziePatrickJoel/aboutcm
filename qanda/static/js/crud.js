 /**
  * 
  * ce module est celui responsable de la création d'un nouvel élément
  * En gros il soumet le formulaire à un controleur
  */

 var App = App || {};

 App.lastResponseData = {};

 App.executeRequest = function(formData, route, contentType, callBack) {
     $.ajax({
             url: route,
             type: 'POST',
             data: formData,
             contentType: contentType,
             cache: false,
             processData: false
         })
         .done(function(data) {
             callBack(data);
         })
         .fail(function() {
             var result = { result: 0, data: ["Erreur côté serveur veuillez contacter l'administrateur"] };
             callBack(result);
         });

 };