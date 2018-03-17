app.controller("displayCtrl", function ($scope, $window, $http, $rootScope) {
    var vm = this;
    vm.yoyo = 123;
    var paramString = "";
    vm.categories = [];
    var now = new Date();
    vm.currentYears = [];
    vm.days = 30;
    vm.searchMode = ['Date', 'Month', 'Year'];
    vm.selectedMode = 'Year';
    vm.tables = ['Products', 'Rating'];
    vm.table = 'Products';

    vm.updateYear = function (currentYear) {
        vm.currentYears = [currentYear - 1, currentYear, currentYear + 1];
        if (vm.currentYears % 4 === 0 && vm.currentMonth === 'February') {
            vm.days = 29;
        }
    };
    vm.monthMapper = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    vm.updateMonth = function (currentMonth) {
        if (currentMonth in ['January', 'March', 'May', 'July', 'August', 'October', 'December']) {
            vm.days = 31;
        }
        else if (currentMonth in ['April', 'June', 'September', 'November']) {
            if (currentMonth in ['January', 'March', 'May', 'July', 'August', 'October', 'December']) {
                vm.days = 30
            }
            else if (currentMonth === "February") {
                vm.days = 28;
                if (vm.currentYears % 4 === 0 && vm.currentMonth === 'February') {
                    vm.days = 29;
                }
            }
        }
    };
    vm.updateDay = function (currentDay) {
        vm.currentDays = [currentDay - 1, currentDay, currentDay + 1]
    };
    vm.updateYear(now.getFullYear());
    vm.currentYear = now.getFullYear();
    vm.currentMonth = vm.monthMapper[now.getMonth()];
    vm.updateDay(now.getDate());
    vm.currentDay = now.getDate();

    vm.search = function () {
        if (vm.selectedMode === 'Year') {
            paramString = 'mode=year&year=' + vm.currentYear;
        }
        else if (vm.selectedMode === 'Month') {
            paramString = 'mode=month&year=' + vm.currentYear;
            paramString = paramString + '&month=' + vm.monthMapper.indexOf(vm.currentMonth);
        }
        else if (vm.selectedMode === 'Date') {
            paramString = 'mode=day&year=' + vm.currentYear;
            paramString = paramString + '&month=' + vm.monthMapper.indexOf(vm.currentMonth);
            paramString = paramString + '&day=' + vm.days;
        }

        var queryString = "http://localhost:8000/dashboard/cat_summary?" + paramString;
        $http.get(queryString).then(
            function success(response) {
                vm.categories = response.data;
            },
            function (response) {
                alert('Failed');
            }
        )
    };

    vm.getData = function () {
        // paramString = 'mode=' +  vm.selectedMode + '&&year=' + vm.currentYears+ '&&day=' + vm.currentDay+ '&&day=' + vm.currentDay;
        var queryString = "http://localhost:8000/dashboard/cat_summary?";
        $http.get(queryString).then(
            function success(response) {
                vm.categories = response.data;
            },
            function (response) {
                alert('Failed');
            }
        )
    };
    vm.getData();

    vm.range = function (min, max, step) {
        step = step || 1;
        var input = [];
        for (var i = min; i <= max; i += step) input.push(i);
        return input;
    };

    vm.updateTable = function (table) {
        if(table==='Rating') {
            getRating();
        }
    };

    var getRating = function () {
        $http.get('http://localhost:8000/api/best_ratings_data/').then(
            function (response) {
                vm.shops = response.data;
            }
        )
    }

});