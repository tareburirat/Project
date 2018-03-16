app.controller('myProductCtrl', function ($scope, $http, $window, $rootScope,$timeout) {
    $scope.products = [];
    $scope.mama = $rootScope.url;
    $scope.sellerId = $window.sellerId;
    $scope.productId = $window.productId;
    var transactionTypeUsage = 2;
    var amount = 10;
    $scope.counter = 100;

    $scope.getId = function (id,coin) {
        $scope.sellerId = id;
        $scope.coin = coin;
        getProduct();
    };




    var getProduct = function() {
        // debugger;
        $http.get($scope.mama + '/api/products/?seller_id=' + $scope.sellerId).then(
            function (response) {
                $scope.products = response.data.results;
            },
            function (response) {
                console.log(response)
            })
    }

    $scope.delProduct = function (productId) {
        $http.delete($scope.mama + '/api/products/' + productId).then(
            function (response) {
                $scope.products = response;
                alert('delete success!!');
                getProduct();
            }
        )
    };

    $scope.promoteProduct = function (product){
        debugger;
        if ($scope.coin < amount){
            alert('จำนวนเหียญไม่พอ');
            return;
        }
        var data = {
            account : product.seller_data.id,
            transaction_type : transactionTypeUsage,
            amount : amount,
            promoted_product : product.id
        };

        $http.post($scope.mama + '/api/coin_transactions/', data).then(
            function success(response) {

                alert('สินค้าชิ้นนี้ถูกโปรโมทแล้ว');
                $window.location.href =  $scope.mama + '/account/my_product/';

            },
            function () {
                alert('fail')
            }

        )
    };

    $scope.onTimeout = function(){
        $scope.counter--;
        mytimeout = $timeout($scope.onTimeout,1000);
    }
    var mytimeout = $timeout($scope.onTimeout,1000);


//     $scope.countDownDate = new Date("Sep 5, 2018 15:00:00").getTime();
//     $scope.setInterval = (function() {
//     $scope.now = new Date().getTime();
//     var distance = countDownDate - now;
//     var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
//     var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
//     var seconds = Math.floor((distance % (1000 * 60)) / 1000);
//     document.getElementById("demo").innerHTML = hours + "h " + minutes + "m " + seconds + "s ";
//     if (distance < 0) {
//         clearInterval(x);
//         document.getElementById("demo").innerHTML = "EXPIRED";
//     }
// }, 1000);




});