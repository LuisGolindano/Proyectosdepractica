class Producto {
  constructor(nombre, precio, año) {
      this.nombre = nombre;
      this.precio = precio;
      this.año = año;
  }
}


class UI {
  addProduct(producto) {
      const productList = document.getElementById('product-list');
      const element = document.createElement('div');
      element.innerHTML = `
          <div class="card text-center mb-4">
              <div class="card-body">
                  <strong>Product</strong>: ${producto.nombre} -
                  <strong>Price</strong>: ${producto.precio} - 
                  <strong>Year</strong>: ${producto.año}
                  <a href="#" class="btn btn-danger" name="delete">Delete</a>
              </div>
          </div>
      `;
      productList.appendChild(element);
  }

  resetForm() {
      document.getElementById('product-form').reset();
  }

  deleteProduct(element) {
      if (element.name === 'eliminar') {
          element.parentElement.parentElement.remove();
          this.showMessage('El producto se a añadido sactisfactoriamente');
      }
  }

  showMessage(mensaje, cssClass) {
      const div = document.createElement('div');
      div.className = `alert alert-${cssClass} mt-2`;
      div.appendChild(document.createTextNode(mensaje));
      const container = document.querySelector('.container');
      const app = document.querySelector('#App');
      container.insertBefore(div, app);
      setTimeout(function () {
          document.querySelector('.alert').remove();
      }, 3000);
  }
}

document.getElementById('product-form')
  .addEventListener('submit', function (e) {

      const nombre = document.getElementById('Nombre').value,
          precio = document.getElementById('Precio').value,
          año = document.getElementById('Año').value;

      const product = new Producto(nombre, precio, año);


      const ui = new UI();


      if (nombre === '' || precio === '' || año === '') {
          ui.showMessage('Por favor insertar un producto');
      }

   
      ui.addProduct(producto);
      ui.showMessage('El producto se a añadido sactisfactoriamente');
      ui.resetForm();

      e.preventDefault();
  });

document.getElementById('product-list')
  .addEventListener('click', function (e) {
      const ui = new UI();
      ui.deleteProduct(e.target);
      e.preventDefault();
  });