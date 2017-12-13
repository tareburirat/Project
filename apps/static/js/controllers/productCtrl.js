(function () {
    'use strict';

    var app = angular.module("app", []);
    app.controller("productCtrl", function($scope, MyService) {
        $scope.product = [];

        MyService.getProduct().then(function (data) {
            $scope.product = data;
        });

}).factory('MyService', function ($http, $q) {
        'use strict';
        return {
            getProduct : function () {
                var deferred = $q.defer();

                $http.get('http://localhost:8000/api/products/').success(function (data) {
                        deferred.resolve(data);
                });
                return deferred.promise;
            }
        };
}).config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});
})();
