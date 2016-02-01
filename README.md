# Blog book

This book is published at [blog.zafar.cc](http://blog.zafar.cc)

Please, visit the website to see the rendered content.

## Structure
The detailed structure of the book is given [here](SUMMARY.md).

### Book structure:
- ROOT directory
    - [Glossary](GLOSSARY.md) → Glossary goes in here
    - [styles](styles) → Put styles here. For details refer to [GitBooks](//help.gitbook.com/styling/book.html).
    - [Introduction](INTRO.md) → This is just an introduction
        - The [introduction](introduction) folder holds extra stuff
    - [Folder] → The folders right under the ROOT directory have to have descriptive names (i.e.: "arrays", "linked_lists", etc.). 
        - The folder has to have a markdown file under it with the same name as the folder itself with the description and basic introduction to the topic (i.e.: "arrays/arrays.md", "linked_lists/linked_lists.md", etc.).
        - [Subfolder] → The subfolders must cover general topics related to the parent folder (i.e.: primer, math, etc.)
            - Subfolder has to have a markdown file with the same name as the subfolder with description and/or tutorials on the subject (i.e.: arrays/math/math.md)

### Solutions structure:
- The solutions are in the [solutions](//github.com/zafartahirov/blog/tree/solutions) branch of the repository. 
- The directory structure has to be the same as the book structure, with the folders in the solutions branch corresponding to the folders in the book. 
    - For example: If there is a question in the book under "arrays/primer/spiral_example.md", the solutions have to be under "arrays/primer/spiral_example/(language)".
- Every solution has to sit under the **(language)** folder: "Python", "C", "C++", "Scala", "Java", etc.
- Every solution has to have a file with the solution, and a "*_test" file, which would hold the unittests.


## Contributors
* [Zafar T.](//resume.zafar.cc)
* [Bob Z.](//github.com/byzhou)

---

If you'd like to contribute to the book, clone the project, make your changes and send a pull request. Note that the pull request will be rejected if not conforming to the structure above.
