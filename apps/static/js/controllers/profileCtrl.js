app.controller("profileCtrl", function($scope, $http, $rootScope) {
    $scope.mama = $rootScope.url;
    $scope.accounts = [];
    
    $http.get($scope.mama + '/api/accounts/').then(function (response) {
        $scope.accounts = response.data;
        console.log($scope.accounts)
    })

});
