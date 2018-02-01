app.controller("addressCtrl", function ($scope, $window, $http, $rootScope) {
    $scope.mama = $rootScope.url;
    $scope.addresses = [];
    $scope.selectedAddress = 0;

    $scope.getBuyerId = function (buyerId) {
        $scope.buyerId = buyerId;
        getBuyerAddresses(buyerId);
    };

    var getBuyerAddresses = function (buyerId) {
        $http.get($scope.mama + '/api/addresses/?buyer_id=' + buyerId).then(
            function success(response) {
                $scope.addresses = response.data;
                $scope.selectedAddress = $scope.addresses.findIndex(function (address) {
                    return address.primary === true;
                });
                console.log($scope.addresses)
            },
            function fail(response) {
                console.log(response);
                alert('Something went wrong, cannot get all addresses!')
            }
        );
    };

    $scope.updatePrimaryAddress = function () {
        var addressId = $scope.addresses[$scope.selectedAddress].id;
        var data = {
            primary: true
        };
        $http.patch($scope.mama + '/api/addresses/' + addressId + '/', data).then(
            function (response) {
                console.log(response);
                alert('success')
            },
            function (response) {
                console.log(response);
                alert('failed');
            }
        );
    };

    $scope.updateSelectedAddress = function (addressId) {
        $scope.selectedAddress = addressId;
    };

    $scope.saveAddress = function () {
        var data = {
            address: $scope.address,
            sub_district: $scope.sub_district,
            district: $scope.district,
            province: $scope.province,
            zip_code: $scope.zip_code,
            buyer: $scope.buyerId
        };

        $http.post($scope.mama + '/api/addresses/', data).then(
            function (response) {
                getBuyerAddresses($scope.buyerId);
                alert('เพิ่มที่อยู่เรียบร้อย');
            },
            function (response) {
                alert("failed: " + response.data)
            }
        )
    };
});