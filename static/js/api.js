const apiUrl = '/api/tracks'
const headers = { 'Content-Type': 'application/json' }

const appData = () => ({
   addMode: true,
   tracks: [],
   editItem: {},
   selectedTrack: {},
   form: {
         id: '',
         title: '',
         artist: '',
         duration: '',
         last_play: ''
   },

   init() {
         this.getTracks()
   },

   getTracks() {
         axios.get(apiUrl)
            .then(response => {
               this.tracks = response.data
            })
   },

   resetForm() {
         this.editItem = {}
   },

   saveData() {
         if (!this.editItem) {
            return
         }
         const bodyData = { ...this.editItem }
         axios.post(apiUrl, bodyData, { headers: headers })
            .then(response => {
               this.tracks = [response.data, ...this.tracks]
               this.resetForm();
               this.getTracks();
            })
   },

   editTrack(track) {
         document.getElementById('myEditModal').classList.toggle('hidden')
         this.addMode = false
         this.form.id = track.id
         this.form.title = track.title
         this.form.artist = track.artist
         this.form.duration = track.duration
         this.form.last_play = track.last_play.replace('Z', '')
   },

   updateData() {
         axios.put(`/api/tracks/${this.form.id}`, this.form)
            .then(response => {
               // Lidar com a resposta, como fechar o modal ou exibir uma mensagem de sucesso
               console.log(response)
               if (response.request.status === 200) {
                     alert(this.form.title + " foi atualizado com sucesso.")

                     // Atualiza os dados da tela
                     this.getTracks();

                     // Fechar Modal
                     var modal = document.getElementById('myEditModal');
                     modal.querySelector('.btn-close').click();
               }
            })
            .catch(error => {
               alert("Ocorreu um erro: " + error)
            });
   },

   cancelEdit() {
         document.getElementById('myEditModal').classList.toggle('hidden')
         this.resetForm()
   },

   deleteItem(track) {
         axios.delete(`/api/tracks/${track.id}`)
            .then((res) => {
               if (res.data.success) {
                     this.tracks.splice(this.tracks.indexOf(track), 1)
               }
            })
            .catch((err) => console.log(err))
   },
})