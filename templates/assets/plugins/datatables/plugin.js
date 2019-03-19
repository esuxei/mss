require.config({
    shim: {
        'datatables': ['jquery', 'core', 'bootstrap']
    },
    paths: {
        "jquery":    "//code.jquery.com/jquery-1.12.4",
        //"dataTables": "/assets/plugins/datatables/js/datatables.min",
        "datatables.net": "/assets/plugins/datatables/js/jquery.dataTables.min",
        "datatables.net-bs4": "/assets/plugins/datatables/js/dataTables.bootstrap4.min",
        "datatables.net-buttons": "/assets/plugins/datatables/js/dataTables.buttons.min",
        "datatables.net-bs4-buttons": "/assets/plugins/datatables/js/buttons.bootstrap4.min",
        "datatables-jszip": "/assets/plugins/datatables/js/jszip.min",
        "datatables-pdfmake": "/assets/plugins/datatables/js/pdfmake.min",
        "datatables-vfs_fonts": "/assets/plugins/datatables/js/vfs_fonts",
        "datatables-buttons-html5": "/assets/plugins/datatables/js/buttons.html5.min",
        "datatables-buttons-print": "/assets/plugins/datatables/js/buttons.print.min",
        "datatables-buttons-colVis": "/assets/plugins/datatables/js/buttons.colVis.min"
    }
});