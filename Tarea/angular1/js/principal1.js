var app = angular.module('app', ['ngRoute','ngResource']);
app.controller("controlador",function ($scope,datos){
   $scope.mensaje="saludos";
   $scope.lista=datos.get();

   $scope.logue=function() {
     var a=$scope.sd;
  	 for (var i = 0; i< $scope.lista.length; i++) {
  	 
  	 	  if(angular.equals(a,$scope.lista[i].cedula)){
            window.location.href="practica13.html";
     	  }else{
            $scope.sd="";
        }
  	 }; 

   }


});
app.factory('datos',['$resource',function($resource){
     return $resource("http://127.0.0.1:8000/alumno/", {},{get:{method:"GET",isArray:true}});

}]);