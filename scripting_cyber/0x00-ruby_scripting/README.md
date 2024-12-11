<strong>0. Hello World with Function</strong><br>
Write a Ruby script that prints “Hello, Holberton! from Ruby!” using a function that accepts one argument String and print Hello, Holberton! from <str>.

    Function prototype: say_hello(str)

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ cat 0-main.rb 
require_relative '0-hello_world_function'

say_hello("Ruby!")
```

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ruby 0-main.rb 
Hello, Holberton! from Ruby!
```
---

<strong>1. Hello World with Class </strong><br>
Class HelloWorld

    Use method that sets an instance
        create variable called message that hold the string Hello World!
    Create a method that display the message called print_hello

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ cat 1-main.rb 
require_relative '1-hello_world_class'

# Create an instance of HelloWorld, change the message, and call the print_hello method
hello_world_instance = HelloWorld.new

hello_world_instance.print_hello
```

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ruby 1-main.rb 
Hello, World!
```
---

<strong>2. Prime Number Checker</strong><br>
Write a function that checks if a given number is prime.

    Function prototype:prime(number)
    Using the Prime Class

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ cat 2-main.rb 
require_relative '2-prime'

puts prime(5)
puts prime(6)
puts prime(7)
puts prime(8)
puts prime(9)
puts prime(10)
puts prime(101)
```

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ruby 2-main.rb 
true
false
true
false
false
false
true
```

---

<strong>3. Reading from a File</strong><br>
Write a Ruby function that reads content from a Json file and count the userId.

    Function Name : count_user_ids(path)

file : file.json

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ cat 3-main.rb
require_relative '3-read_file'

count_user_ids('file.json')
```

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ruby 3-main.rb 
1: 10
2: 8
3: 11
4: 13
5: 7
6: 4
7: 9
8: 8
9: 2
10: 1
```

---

<strong>4. Writing to a File</strong><br>
Write a Ruby function merge_json_files that merges JSON objects from one file into another.

file : file.json

    Function prototype:merge_json_files(file1_path, file2_path)

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ cat 4-main.rb
require_relative '3-read_file'
require_relative '4-write_file'

file1_path = 'file_to_copy_from.json'
file2_path = 'file.json'


merge_json_files(file1_path, file2_path)


puts 'File merged successfully!'

count_user_ids(file2_path)
```

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ruby 4-main.rb
1: 10
2: 8
3: 11
4: 13
5: 7
6: 4
7: 10
8: 8
9: 2
10: 1
11: 2
12: 1
13: 4
```

---

<strong> 5. Implementing a Caesar Cipher Encryption and Decryption using Classes</strong><br>
Create a Ruby program using classes to encrypt and decrypt messages using the Caesar cipher technique.

    CaesarCipher Class: Define a class CaesarCipher with the following methods:
        initialize(shift): Constructor that initializes the shift value (shift) for encryption and decryption.
        encrypt(message): Method that takes a plaintext message (message) and returns the encrypted message using the Caesar cipher technique with the specified shift.
        decrypt(message): Method that takes a ciphertext message (message) and returns the decrypted message using the Caesar cipher technique with the specified shift.
        cipher(message, shift) : Method in a Caesar cipher implementation encrypts or decrypts a given message string based on the shift value provided
            Can only be called from within the same instance

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ cat 5-main.rb
require_relative '5-cipher'


cipher = CaesarCipher.new(5)

# Encrypting a message
plaintext = "Hello, Holberton!"
encrypted_message = cipher.encrypt(plaintext)
puts "Encrypted message: #{encrypted_message}"

# Decrypting the encrypted message
decrypted_message = cipher.decrypt(encrypted_message)
puts "Decrypted message: #{decrypted_message}"
```

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ruby 5-main.rb
Encrypted message: Mjqqt, Mtqgjwyts!
Decrypted message: Hello, Holberton!
```

---

<strong>6. Simple HTTP Request</strong><br>
Create a Ruby function get_request(url) that performs an HTTP GET request to the specified url and prints the response status code and body the output should be as shown bellow in json Format

Method : get_request(url)

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ cat 6-main.rb
require_relative '6-get'

get_request('http://jsonplaceholder.typicode.com/posts/1')
```

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ruby 6-main.rb
Response status: 200 OK
Response body:
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
```

---

<strong>7. Command-Line Arguments</strong><br>
Create a Ruby script that accepts command-line arguments and prints each argument.

    Method: print_arguments

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ cat 7-main.rb
require_relative '7-args'

print_arguments
```

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ruby 7-main.rb
No arguments provided.
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ruby 7-main.rb arg1 arg2 arg3
1. arg1
2. arg2
3. arg3
```

---

<strong>8. HTTP POST Request</strong><br>
Write a Ruby script that makes an HTTP POST request to a specified URL with optional body parameters and prints the response.

    Method: post_request
        Parameters:
            url
            body_params

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ cat 8-main.rb
require_relative '8-post'

url = 'https://jsonplaceholder.typicode.com/posts'
body_params = { title: 'Try to Post', body: "Okay that's good", userId: 11, id: 101 }
post_request(url, body_params)
```

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ruby 8-main.rb
Response status: 201 Created
Response body:
{
  "title": "Try to Post",
  "body": "Okay that's good",
  "userId": 11,
  "id": 101
}
```

---

<strong>9. Downloading a File</strong><br>
Write a Ruby script that accept two args the URL and the Path to download a file from a given URL and saves it locally using open-uri, uri, fileutils.

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ls
9-download_file.rb
```

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ruby 9-download_file.rb
Usage: 9-download_file.rb URL LOCAL_FILE_PATH
```

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ruby 9-download_file.rb https://logowik.com/content/uploads/images/ruby6530.jpg ./ruby6530.jpg
Downloading file from https://logowik.com/content/uploads/images/ruby6530.jpg...
File downloaded and saved to ./ruby6530.jpg.
```

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ls
9-download_file.rb  ruby6530.jpg
```

---

<strong>10. Password Cracker</strong><br>
Write a Ruby script that accepting two args hashed_password dictionary_file to perform a dictionary attack to crack a hashed password.

| Word       | SHA-256 Hash                                                                 |
|------------|-------------------------------------------------------------------------------|
| password   | 5e884898da28047151d0e56f8dc6292773603d0d6aabbddf554a4febe4e60ab3           |
| 123456     | 8d969eef6ecad3c29a3a629280e686cff8fabd2dfd771eebc9bc1696ec3e9d39           |
| qwerty     | d8578edf8458ce06fbc5bb76a58c5ca4a0a8cdd3d44f1e01c8a160d7038b1a5c           |
| admin      | 8c6976e5b5410415bde908bd4dee15dfb16a4d96a35b7c4d465f9c74879ab0d4           |
| welcome    | 25f9e794323b453885f5181f1b624d0b004d6e1d78d9e8a74b1e21610029a450           |


```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ cat dictionary.txt
password
123456
qwerty
admin
welcome
```

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ruby 10-password_cracked.rb 8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918 dictionary.txt
Password found: admin
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ruby 10-password_cracked.rb 76e5b5410415bde908bd4dee15dfb16a4d96773603d0d6aabbddf dictionary.txt
Password not found in dictionary.
```

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ruby 10-password_cracked.rb
Usage: 10-password_cracked.rb HASHED_PASSWORD DICTIONARY_FILE
```

---

<strong>11. Creating a Basic CLI Application</strong><br>
Write a Ruby script to create a basic command-line interface (CLI) application using optparse.

```shell
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ./11-cli.rb -h
Usage: cli.rb [options]
    -a, --add TASK                   Add a new task
    -l, --list                       List all tasks
    -r, --remove INDEX               Remove a task by index
    -h, --help                       Show help
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ./11-cli.rb -a Task1
Task 'Task1' added.
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ cat tasks.txt 
Task1
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ./11-cli.rb -a Task2
Task 'Task2' added.
┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ./11-cli.rb -l
1. Task1
2. Task2
 ┌──(imen㉿hbtn-lab)-[…/scripting_cyber/0x00-ruby_scripting]
└─$ ./11-cli.rb -r 2
Task 'Task2' removed.
```

