app.controller("addressCtrl", function ($scope, $window, $http) {
    $scope.mama = 123;

    $scope.getBuyerId = function (buyerId) {
        $scope.buyerId = buyerId;
    };
    $scope.getAddress = function () {
        var data = {
            address: $scope.address,
            sub_district: $scope.sub_district,
            district: $scope.district,
            province: $scope.province,
            zip_code: $scope.zip_code,
            buyer: $scope.buyerId
        };

        $http.post('http://localhost:8000/api/addresses/', data).then(
            function (response) {
                alert('success!');
                $window.location.href = '/address_buyer/';
            },
            function (response) {
                alert("failed: " + response.data)
            }
        )
    }

});