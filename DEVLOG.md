

***THE BELOW HAS BEEN COPIED FROM OUR HACK CLUB'S CORAL HACKATHON PROJECT'S DEVLOG PAGE***
---------------------------------

*****theodd1isoutman56
Nov 21, 2026
29m tracked*****

made the first initial prototype!!

I haven't made the UI yet and worked on the music engine too much (my friend Harinesh is actually on the UI) but i made something super basic and im proud of it!!

i watched a video of some guy explaining pygame to me and i used his advice

it currently plays music once i enter the path to the file and the controls are simple numbers. CLI based [for now]

<img width="1103" height="363" alt="image" src="https://github.com/user-attachments/assets/4f5d4e07-b791-4f59-8e01-6fc53aff1a14" />

-Kashyap :>


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*****harinesh.sv
Nov 21, 2026
27m tracked*****

so basically made the ui for the project and we are trying to go for a fruitiger -aero typa design hopefully we finish it

<img width="1486" height="940" alt="image" src="https://github.com/user-attachments/assets/10ea0236-a098-4401-9ad8-d20a7e0ebf0b" />

-Harinesh :P

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*****harinesh.sv
Nov 21, 2026
24m tracked*****

added background yayy
i change background to the new frutiger aero thing... i think it looks pretty cool what do yall think about it

<img width="1506" height="939" alt="image" src="https://github.com/user-attachments/assets/df389b18-5703-48d4-84fe-77e121d82d7e" />

-Harinesh :P

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*****theodd1isoutman56
Nov 21, 2026
1h 32m tracked*****

I added the ability to make playlists, go back and forth between songs in said playlist, songs autoplaying to the next song while in playlist, previous and next looping to the original song once they reach the end of the playlist, songs saving in the playlist so that it is still accessible once left and reopened, and a WIP album metadata shower which is being debugged.

The plan is that i take care of the music engine and Harinesh takes care of the UI, and towards the end we sort of fuse them together to create our final product :P

<img width="860" height="295" alt="image" src="https://github.com/user-attachments/assets/9802d349-1f6e-4f0a-a29b-7de51a189f12" />


<img width="1313" height="363" alt="image" src="https://github.com/user-attachments/assets/c18ebbe2-416b-4f0f-8c5d-f8e684f7bc8b" />


right now the Metadata thing (which im using Mutagen for) is super bugged and returns a lot of binary junk (as seen below) when i put in an mp3 file that i know has some metadata in it

<img width="1911" height="782" alt="image" src="https://github.com/user-attachments/assets/b7d249fb-5f03-4d40-ade9-94f4c3101fb4" />


Im gonna go to bed now, tommorow ill definitely fix the metadata thing and add a lot more features. Ill also help Harinesh out with whatever things he needs in the UI part

the music engine is almost completely done in PyGame.

-Kashyap :>

-------

*****theodd1isoutman56
Nov 22, 2026
1h 44m tracked*****

**Added some more features, fixed some old bugs, found some new bugs [removing songs from playlist, clear, shuffle]**

Hello! Ive added some more features. I've also fixed the bug i had from earlier where Mutagen was showing binary instead of album metadata. It was fixed by switching from its raw ID3 to easyID3, which let it easily access basic album metadata including album name, artist name, album art (coming soon), and duration

the features are:

Removing tracks one by one from playlist [ removesong() ] It shows the whole playlist (numbered) so you can choose, via number, which one you want to get rid of. Choosing a number deletes the track from from the instance youre running right now (memory) as well as .json storage
<img width="793" height="566" alt="image" src="https://github.com/user-attachments/assets/c1f15da4-4646-493e-8060-f3e27920db4b" />


added input vaildations so the program recognises if youve put in an unexpected value and provides an appropriate response for it

<img width="702" height="111" alt="image" src="https://github.com/user-attachments/assets/9b9763a7-f33b-4e7c-8727-a12d6a5f4ff3" />


clearing the whole playlist [ clearplaylist() ] When the option is selected, the entire playlist is cleared, and set that way in .json storage. Resets current_index to -1 and standalone_song to none (cuz its being cleared, duh)
<img width="271" height="92" alt="image" src="https://github.com/user-attachments/assets/3ff9b32c-7c89-49ef-a89f-4ad524ef916c" />


shuffle [ songshuffle() ] I used pythons random module for this. I've never really used it much before, so i did need some help from AI for debugging and as a base to get me started.
When shuffle is enabled, it adds random starting-track selections

<img width="882" height="130" alt="image" src="https://github.com/user-attachments/assets/10e66e48-11ef-4cae-9b79-98e33ca4d6f1" />




as of right now, the only thing that works with shuffle is next(), meaning when shuffle is enabled and you start to play your playlist, pressing next will shift to the next song in a completely random manner.

<img width="1011" height="669" alt="image" src="https://github.com/user-attachments/assets/934a79e2-a162-45c7-8055-1ed9105f25a4" />



i DID code a little something so that it becomes shuffled when you play the playlist as normal too, but i guess it got bugged or something since it isnt working up to my standard. Ill be sure to fix this before my next log!

I also need to fix a double increment bug in next() that cause tracks to randomly skip while playing back. which i will surely do next.

i also added a check in play() so that nonexistant selections will not be attempted to be loaded in.

Thats all for now! See you in my next log :P

P.S. Harinesh has a lot of schoolwork to catch up on so it might be a while before his next log P.P.S. Right now the both of us have different main.py(s) and player.py(s), since were in the same repo, but in different branches. Once were happy with our respective engine and ui, we'll merge his UI into the main branch with me, and with that our project will exit the prototype stage. So until then, its going to be like were working on different projects haha.

Anyway, props if you took the time to read all this Catch you later!

Kashyap :>
