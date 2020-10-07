//loadTable
$(document).ready(function(){
    var table = $('#customerDataTable').DataTable({
        "dom": "<'row'<'col-sm-12 col-md-3'l><'col-sm-12 col-md-3 d-flex datefrombar'><'col-sm-12 col-md-3 d-flex datetobar'><'col-sm-12 col-md-3'f>>" +
        "<'row'<'col-sm-12'tr>>" +
        "<'row'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-2'B><'col-sm-12 col-md-2 addCustomerBar'><'col-sm-12 col-md-3'p>>",
        "oLanguage": {
            "sSearch": "Search:"
          },
        //buttons: ['excel'],
        // exportOptions : {
        //     columns: 'th:not(:last-child)'
        // },
        buttons: [
            {
               extend: 'excel',
               text: 'Excel',
               className: 'btn btn-success btn-block excelButton',
               exportOptions: {
                  columns: 'th:not(:last-child)'
               }
            }
         ],
        "columnDefs": [
            { "orderable": false, "targets": 5 }
        ]
    });
    $(".excelButton").parent().addClass("container p-0");
    //table.buttons().container().appendTo( '#menuBar' );
    var datefrom = '<span class="date-label mr-1 mt-1">From:</span><input type="date" class="form-control form-control-sm" id="datefrom"><i class="material-icons mt-1" id="clearfrom">close</i>';
    var dateto = '<span class="date-label mr-1 mt-1">To:</span><input type="date" class="form-control form-control-sm" id="dateto"><i class="material-icons mt-1" id="clearto">close</i>';
    var addCustomerButton = '<a class="btn btn-block btn-primary" id="addProduct" href="registration">Add Product</a>';
    $(".datefrombar").append(datefrom);
    $(".datetobar").append(dateto);
    $(".addCustomerBar").append(addCustomerButton);
    $("#clearfrom").css("cursor","default").click(function(){ $("#datefrom").val(""); table.draw(); });
    $("#clearto").css("cursor","default").click(function(){ $("#dateto").val(""); table.draw(); });
    $.fn.dataTable.ext.search.push(
        function (settings, data, dataIndex) {
            var min = $('#datefrom').val();
            var max = $('#dateto').val();
            //var max = $('#dateto').datepicker('getDate');
            //var startDate = new Date(data[0]);
            var startDate = data[0];
            //alert(min+" "+startDate+" "+max);
            if (min == "" && max == "") return true;
            if (min == "" && startDate <= max) return true;
            if (max == "" && startDate >= min) return true;
            if (startDate <= max && startDate >= min) return true;
            return false;
        }
    );
    //$('#datefrom').datepicker({ onSelect: function () { table.draw(); } });
     $('#datefrom').select(function(){ table.draw(); });
     $('#dateto').select(function(){ table.draw(); });
    //$('#dateto').datepicker({ onSelect: function () { table.draw(); } });
    $('#datefrom, #dateto').change(function () {
        table.draw();
    });
});

$(".deleteColor").click(function(){
    $("#deleteModal").modal('show');
    var viewInfo = $(this).parent().siblings();

    $("[name=product-sku]").val($(viewInfo[6]).html());

});

$(".viewColor").click(function(){
    $("#viewModal").modal('show');
    var viewInfo = $(this).parent().siblings();

    $("[name=dateRegField]").val($(viewInfo[0]).html());
    $("[name=categoryField]").val($(viewInfo[1]).html());
    $("[name=brandField]").val($(viewInfo[2]).html());
    $("[name=nameField]").val($(viewInfo[3]).html());
    $("[name=priceField]").val($(viewInfo[4]).html());
    $("[name=stocksField]").val($(viewInfo[5]).html());
    $("[name=skuField]").val($(viewInfo[6]).html());
    $("[name=colorField]").val($(viewInfo[7]).html());
    $("[name=lengthField]").val($(viewInfo[8]).html());
    $("[name=widthField]").val($(viewInfo[9]).html());
    $("#profDisplay").attr("src", $(viewInfo[10]).html());
    $("#profDisplay1").attr("src", $(viewInfo[11]).html());
    $("#profDisplay2").attr("src", $(viewInfo[12]).html());
});



function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#profDisplay').attr('src', e.target.result)
        };
        reader.readAsDataURL(input.files[0]);
    }
}

function readURL1(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#profDisplay1').attr('src', e.target.result)
        };
        reader.readAsDataURL(input.files[0]);
    }
}

function readURL2(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#profDisplay2').attr('src', e.target.result)
        };
        reader.readAsDataURL(input.files[0]);
    }
}