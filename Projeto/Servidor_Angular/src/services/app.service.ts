import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AppService {

  apiUrl = 'http://127.0.0.1:5000';

  constructor(
    private httpClient: HttpClient
  ) { }

  downloadDocxFile(data: string) {

    const options = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
      responseType: 'blob' as 'json', // Indica que a resposta deve ser tratada como um objeto Blob
    };
    
    const body = {
      texto: data
    }
    
    this.httpClient.post(this.apiUrl , body, options).subscribe(response => {
      this.saveFile(response);
    });
  }

  saveFile(blob: any) {
    const downloadLink = document.createElement('a');
    downloadLink.href = window.URL.createObjectURL(blob);
    downloadLink.download = 'DocSQL.docx';

    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
  }
}
