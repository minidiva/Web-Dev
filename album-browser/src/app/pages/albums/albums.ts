import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { AlbumService } from '../../core/services/album.service';
import { Album } from '../../core/models/album';

@Component({
  selector: 'app-albums',
  templateUrl: './albums.html',
  standalone: true,
  imports: [CommonModule, RouterModule]
})
export class Albums implements OnInit {
  albums: Album[] = [];
  loading = true;

  constructor(
    private albumService: AlbumService,
    private cd: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.albumService.getAlbums().subscribe({
      next: data => {
        this.albums = data;
        this.loading = false;
        this.cd.detectChanges();
      },
      error: err => {
        console.error(err);
        this.loading = false;
        this.cd.detectChanges();
      }
    });
  }

  deleteAlbum(id: number) {
    this.albumService.deleteAlbum(id).subscribe(() => {
      this.albums = this.albums.filter(a => a.id !== id);
      this.cd.detectChanges();
    });
  }
}