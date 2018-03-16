app.controller("addCoinsCtrl", function ($scope, $window, $http, $rootScope) {
    $scope.mama = $rootScope.url;
    $scope.coin_transactions = [];
    $scope.mama12 =123;
    var transactionTypeUsage = 0;

    $scope.getId = function (id) {
        $scope.sellerId = id;
        getCoinsTransactions();
    };

    var getCoinsTransactions = function() {
        $http.get($scope.mama + '/api/coin_transactions/?account=' + $scope.sellerId).then(
            function (response) {
                $scope.products = response.data.results;
            },
            function (response) {
                console.log(response)
            })
    }



    $scope.saveAddCoins = function (){
        var data = {
            account : $scope.sellerId,
            transaction_type : transactionTypeUsage,
            amount : $scope.amount,
        };

        $http.post($scope.mama + '/api/coin_transactions/', data).then(
            function success(response) {
                alert('เรียบร้อย')
                $window.location.href =  $scope.mama + '/account/coins/';

            },
            function () {
                alert('fail')
            }

        )
    };
});