app.controller("profileCtrl", function($scope, $http) {
    $scope.mama = 12345;
    $scope.accounts = [];
    
    $http.get('http://localhost:8000/api/accounts/').then(function (response) {
        $scope.accounts = response.data;
        console.log($scope.accounts)
    })

});
