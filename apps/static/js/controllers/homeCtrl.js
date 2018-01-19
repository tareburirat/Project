app.controller("homeCtrl", function ($scope, $http) {
    $scope.mama = 123;
    $scope.products = [];
    console.log(11111111111111111111);
    $http.get('http://localhost:8000/api/products/').then(function (response) {
        $scope.products = response.data;
        console.log($scope.products);
    })

});