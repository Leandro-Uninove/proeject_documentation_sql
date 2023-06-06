import { Component, OnInit } from '@angular/core';
import { AppService } from 'src/services/app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'sql-doc-generator';

  instructionIsVisible: boolean = true;

  constructor(
    private appService: AppService
  ) { }

  ngOnInit(): void {
  }

  myFunction() {
    this.instructionIsVisible = false
    let texto;

    var textarea = document.getElementById('text-area') as HTMLTextAreaElement;
    var inputText = textarea.value;

    texto = inputText;
    texto.toUpperCase();

    if (texto.includes('CREATE TABLE' && ';')) {
      this.appService.downloadDocxFile(texto);
    }

  }
}
