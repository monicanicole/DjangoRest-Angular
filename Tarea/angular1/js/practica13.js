var app = angular.module('app', ['ngRoute','ngResource']);
app.controller("controlador",function ($scope,datos){
   $scope.mensaje="saludos";
   $scope.lista=datos.get();


	$scope.mostrar=function(){
		$scope.boton=true;
	}
	
   $scope.restar=function(parametro) {
   		
   		if ($scope.lista[parametro].cupos>0) {
   		$scope.lista[parametro].cupos=parseInt($scope.lista[parametro].cupos)-1;
   		}else{
   			alert("no puedes matricularte");
   		}
   		
    }

});
app.factory('datos',['$resource',function($resource){
     return $resource("http://127.0.0.1:8000/materia/", {},{get:{method:"GET",isArray:true}});

}]);

