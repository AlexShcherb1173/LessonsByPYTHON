{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": True
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AlexShcherb1173/helloworld/blob/master/%D0%A3%D1%80%D0%BE%D0%BA_7_2.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ZPd6puitv6LE"
      },
      "source": [
        "## Множества (set)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IbuIZPPFMGnd"
      },
      "source": [
        "Set — это набор, или, как еще его называют, множество. Первое, что нужно знать, — в нем не может быть повторяющихся элементов.\n",
        "\n",
        "Второе — он пишется в фигурных скобках"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fLboo_JPsnZN",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2943ed28-ac7d-410c-d855-743a69430f9c"
      },
      "source": [
        "my_languages = {\"Python\", \"Java\", \"Go\", \"Python\", \"Go\"}\n",
        "\n",
        "print(len(my_languages))\n",
        "\n",
        "print(my_languages)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "3\n",
            "{'Go', 'Java', 'Python'}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2t8EKP3hOEzt"
      },
      "source": [
        "Из-за этой особенности его часто используют, чтобы уникализировать списки."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QQTZvekOOQlw",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f3469aaa-738e-4a7a-b607-c96ccc459e97"
      },
      "source": [
        "my_languages = [\"Python\", \"Java\", \"Go\", \"Python\", \"Go\"]\n",
        "\n",
        "my_unique_languages = set(my_languages)\n",
        "\n",
        "print(list(my_unique_languages))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "['Go', 'Java', 'Python']\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fJeqxHc3OIwj"
      },
      "source": [
        "Множества не упорядочены, поэтому индексов и слайсов у них нет."
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "gH2LJqJJ-1mc"
      }
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aCi2jJgPO3OR"
      },
      "source": [
        "my_languages = {'Go', 'Java', 'Python'}\n",
        "print(my_languages)\n",
        "print(my_languages[1]) # Тут будет ошибка"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wbTtKj4LSF3O"
      },
      "source": [
        "А теперь — плохие новости от компьютера: передать несколько элементов в set не получится. А если передать строку, он разобьет ее по буквам."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xvZr8lHBSR52",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "45fb583f-76af-49c2-8f39-d4e26abe0a9c"
      },
      "source": [
        "surprise = set('Python')\n",
        "print(surprise)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "{'P', 'h', 't', 'o', 'y', 'n'}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LBwUNZjrOJ1c"
      },
      "source": [
        "В остальном set похож на список: у него тоже есть методы.\n",
        "\n",
        "Не запоминайте их — не пригодится. Запишите на стикере и применяйте при необходимости."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SmkldLeoPzkm",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "111abc88-3910-4c98-c326-450b7a6b15b9"
      },
      "source": [
        "# add - добавляет элемент в множество. Не спрашивайте почему не append\n",
        "\n",
        "my_languages = {'Go', 'Java', 'Python'}\n",
        "\n",
        "my_languages.add('Swift')\n",
        "print(my_languages)\n",
        "\n",
        "my_languages.add('Ruby')\n",
        "print(my_languages)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "{'Python', 'Java', 'Go', 'Swift'}\n",
            "{'Java', 'Go', 'Swift', 'Python', 'Ruby'}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IemQAxmJQUKC",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e8d37b6e-792d-47f6-b8de-b69d289c738e"
      },
      "source": [
        "# pop — удаляет первый элемент из множества и возвращает его. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.\n",
        "\n",
        "my_languages = {'Go', 'Java', 'Python'}\n",
        "my_languages.pop()\n",
        "language = my_languages.pop()\n",
        "print(language)\n",
        "print(my_languages)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Java\n",
            "{'Go'}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2Ba8RnGMQjVO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "28bc623c-6580-46f6-9bdc-bcb68ec41677"
      },
      "source": [
        "# discard — удаляет элемент, если он находится в множестве.\n",
        "\n",
        "my_languages = {'Go', 'Java', 'Python'}\n",
        "my_languages.discard('Go')\n",
        "my_languages.discard('Ruby')\n",
        "print(my_languages)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "{'Python', 'Java'}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oiwTGjfWQ1Ce",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ce121364-72d2-4d96-861c-4a909fc78708"
      },
      "source": [
        "# remove — тоже удаляет элемент из множества. KeyError, если такого элемента не существует.\n",
        "\n",
        "my_languages = {'Go', 'Java', 'Python'}\n",
        "my_languages.remove('Go')\n",
        "print(my_languages)\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "{'Python', 'Java'}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5Mt7-hu4ReYZ"
      },
      "source": [
        "Ну и, конечно, по набору можно запускать цикл:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PG-QrIXaRlvN",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "78d527e0-ab06-4f3f-8c7c-1bd46dc4fb74"
      },
      "source": [
        "my_languages = {'Go', 'Java', 'Python'}\n",
        "\n",
        "for lang in my_languages:\n",
        "  print(lang)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Python\n",
            "Java\n",
            "Go\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "oIavcND6Rhrt"
      },
      "source": [
        "На самом деле множества используются для специфических задач пересечения. Вот смотрите:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "19B1UNnoToh8"
      },
      "source": [
        "# union — это сложение или объединение, например мне нужно выучить к моим языкам еще и языки фронтенда\n",
        "\n",
        "my_languages = {'Go', 'Java', 'Python', 'HTML', 'CSS'}\n",
        "frontend = {'HTML', 'CSS', 'JavaScript'}\n",
        "\n",
        "my_languages.union(frontend)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "djsJ7Ql4Ueim"
      },
      "source": [
        "# intersection — это пересечение, например какие из языков, которые я знаю, — фронтендерские\n",
        "\n",
        "my_languages = {'Go', 'Java', 'Python', 'HTML', 'CSS'}\n",
        "frontend = {'HTML', 'CSS', 'JavaScript'}\n",
        "\n",
        "my_languages.intersection(frontend)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "no_KVuIpUqgQ"
      },
      "source": [
        "# difference — это вычитание, например какие из языков я знаю КРОМЕ фронтендерских\n",
        "\n",
        "my_languages = {'Go', 'Java', 'Python', 'HTML', 'CSS'}\n",
        "frontend = {'HTML', 'CSS', 'JavaScript'}\n",
        "\n",
        "my_languages.difference(frontend)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "If6IVxh4U1_2"
      },
      "source": [
        "# issubset — возвращает булев тип, сообщает, содержатся ли языки фронтенда полностью в моих языках, то есть знаю ли я все языки фронтенда\n",
        "\n",
        "my_languages = {'Go', 'Java', 'Python', 'HTML', 'CSS'}\n",
        "frontend = {'HTML', 'CSS'}\n",
        "\n",
        "frontend.issubset(my_languages)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6YyMQZgnwAtF"
      },
      "source": [
        "### Задача. Множества"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gyreWD8hwDtz"
      },
      "source": [
        "У вас есть список навыков разработчика. Выписать:\n",
        "\n",
        "- Каких фронтенд-навыков ему не хватает?\n",
        "- Какие бекенд-навыки у него есть?\n",
        "- Какие его навыки не относятся ни к фронтенду, ни к бекенду?\n",
        "- Все ли нужные софт-скилы у него есть?\n",
        "- Какие навыки надо иметь, чтобы быть фулстеком (знать и фронт, и бек)?\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yRfSpYhCv4pT",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "68794f3a-0423-45ee-b083-613e45480aba"
      },
      "source": [
        "my_skills = {\"python\", \"flask\", \"django\", \"критическое мышление\", \"планирование\", \"переговоры\", \"html\", \"css\"}\n",
        "backend_skills = {\"linux\", \"terminal\", \"python\", \"flask\", \"django\", \"restapi\"}\n",
        "frontend_skills = {\"html\", \"css\", \"javascript\"}\n",
        "soft_skills = {\"презентация\", \"планирование\", \"переговоры\", \"лидерство\", \"критическое мышление\"}\n",
        "\n",
        "frontend_i_lack = frontend_skills.difference(my_skills) # Каких фронтенд-навыков ему не хватает?\n",
        "backend_i_have = my_skills.intersection(backend_skills) # Какие бекенд-навыки у него есть?\n",
        "non_tech_skills = my_skills.difference(backend_skills).difference(frontend_skills) # не фронтенд и не бекенд\n",
        "are_softskills_covered = soft_skills.issubset(my_skills) # Все ли софт-скиллы у него есть?\n",
        "fullstack = backend_skills.union(frontend_skills) # навыки для fullstack-разработки\n",
        "\n",
        "print(frontend_i_lack)\n",
        "print(backend_i_have)\n",
        "print(non_tech_skills)\n",
        "print(are_softskills_covered)\n",
        "print(fullstack)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "{'javascript'}\n",
            "{'python', 'django', 'flask'}\n",
            "{'критическое мышление', 'планирование', 'переговоры'}\n",
            "False\n",
            "{'terminal', 'python', 'html', 'javascript', 'flask', 'restapi', 'css', 'django', 'linux'}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "AhuoA5QyXHfq"
      },
      "source": [
        "## Кортежи (tuple)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1YXQeyhPXOLh"
      },
      "source": [
        "Создать кортеж очень просто. Нужно взять список и поменять скобки:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qEPlKctg8-PC",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c6263cc6-4b7e-4382-9393-9e0bc7e138d1"
      },
      "source": [
        "colors = (\"red\", \"green\", \"blue\")\n",
        "type(colors)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "tuple"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 90
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0Lh4FWcH9AN9"
      },
      "source": [
        "Или взять список и превратить его в кортеж:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4lpKUBlS9COg"
      },
      "source": [
        "colors = tuple([\"red\", \"green\", \"blue\"])\n",
        "type(colors)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QG2JyYlr9D5U"
      },
      "source": [
        "Кортеж поддерживает методы и операторы списка, которые не приводят к его изменению (мутации)."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ldwzcNsI9F06"
      },
      "source": [
        "colors = (\"red\", \"green\", \"blue\")\n",
        "\n",
        "len(colors)\n",
        "\n",
        "colors[0]; colors[-1]; colors[:2]\n",
        "\n",
        "colors.index(\"green\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "JL1OH8P_9Hzz"
      },
      "source": [
        "И перебор, конечно.\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fY0eHqlc9Jtu",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e5456384-d8c1-4ff8-85b3-3c447b13becb"
      },
      "source": [
        "colors = (\"red\", \"green\", \"blue\")\n",
        "\n",
        "for color in colors:\n",
        "  print(color)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "red\n",
            "green\n",
            "blue\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "isqD1st09LZ4"
      },
      "source": [
        "А вот любые методы изменения сразу вызовут ошибку:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hJG_ixr59NcT"
      },
      "source": [
        "colors = (\"red\", \"green\", \"blue\")\n",
        "\n",
        "# del colors[0]\n",
        "# colors[0] = None\n",
        "# colors.remove(\"red\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MVss-CEm9RPO"
      },
      "source": [
        "Теперь о хорошем: у кортежей есть фича с возвращением значения из функции, например:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Z8KrPyRK9Tf8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b3206aad-ba6a-4d8d-9a74-3d3ca43f10c0"
      },
      "source": [
        "def daylight():\n",
        "\n",
        "  sunrise = \"6:30\"\n",
        "  sunset = \"22:10\"\n",
        "  return sunrise, sunset\n",
        "\n",
        "\n",
        "start, finish = daylight()\n",
        "print(start)\n",
        "print(finish)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "6:30\n",
            "22:10\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7aj-F0sfaML4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "240f3139-1fa5-43e1-b51d-6dca107230a6"
      },
      "source": [
        "# На самом деле кортеж определяется не скобками, а запятыми\n",
        "\n",
        "tupl123 = (1, 2, ) # Скобок нет, но это кортеж\n",
        "print(tupl123, type(tupl123))\n",
        "\n",
        "one = (1,)  # Скобки есть, но это не кортеж, а просто число 1\n",
        "print (one, type(one))\n",
        "\n",
        "tuple1 = (1,)  # А вот это кортеж, состоящий из одного элемента\n",
        "print (tuple1, type(tuple1))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "(1, 2) <class 'tuple'>\n",
            "(1,) <class 'tuple'>\n",
            "(1,) <class 'tuple'>\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cOVlVNRa9VfK"
      },
      "source": [
        "### Задача. Кортежи"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "n_kypEvA9YAj"
      },
      "source": [
        "Напишите функцию, которая вернет из одной строки Ф. И. О.  так, чтобы можно было сразу использовать их в трех разных переменных.\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qfs2h35s9Z4C",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ccd2c87b-c77f-4490-ce2b-c961082c9829"
      },
      "source": [
        "# Исходный код\n",
        "\n",
        "def fullname_split(fullname_str):\n",
        "  fullname_list = fullname_str.split(' ')\n",
        "\n",
        "  surname = fullname_list[0]\n",
        "  name = fullname_list[1]\n",
        "  patronymic = fullname_list[2]\n",
        "\n",
        "  return (surname, name, patronymic)\n",
        "\n",
        "surname, name, patronymic = fullname_split(\"Гаврилов Юлиан Александрович\")\n",
        "print(name)\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Юлиан\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QxgkHDzOwzoA"
      },
      "source": [
        "## Списки словарей"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Ckyc3Z-sFbCY"
      },
      "source": [
        "Мы знаем, что словарь можно положить в список. Например, список продуктов в магазине:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YDkzYwMN9Rmp"
      },
      "source": [
        "# {\"name\":\"Яблоки\", \"price\":\"100\", \"available\": 40}\n",
        "\n",
        "store = [\n",
        "    {\"name\":\"Яблоки\", \"price\":\"100\", \"available\": 40},\n",
        "    {\"name\":\"Апельсины\", \"price\":\"200\", \"available\": 20},\n",
        "    {\"name\":\"Гранаты\", \"price\":\"400\", \"available\": 5},\n",
        "]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QGvbZDPU-Eai"
      },
      "source": [
        "Но как потом с ними работать? Можно использовать две пары квадратных скобок, вот так:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NUp2sXLQ-Gj4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "383a9dad-82f2-4c6e-b43f-8605ac2c0948"
      },
      "source": [
        "store = [\n",
        "    {\"name\":\"Яблоки\", \"price\":\"100\", \"available\": 40},\n",
        "    {\"name\":\"Апельсины\", \"price\":\"200\", \"available\": 20},\n",
        "    {\"name\":\"Гранаты\", \"price\":\"400\", \"available\": 5},\n",
        "]\n",
        "\n",
        "print(store[0][\"name\"], store[0][\"price\"])\n",
        "print(store[1][\"name\"], store[1][\"price\"])\n",
        "print(store[2][\"name\"], store[2][\"price\"])\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Яблоки 100\n",
            "Апельсины 200\n",
            "Гранаты 400\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wLUgFLFw-the"
      },
      "source": [
        "С помощью двойных скобок можно управлять и содержимым словарей:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hL_1xOWB-4ua",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1d78678b-8c4c-4e2b-8e9b-0d6acbd0ee33"
      },
      "source": [
        "store = [\n",
        "    {\"name\":\"Яблоки\", \"price\":\"100\", \"available\": 40},\n",
        "    {\"name\":\"Апельсины\", \"price\":\"200\", \"available\": 20},\n",
        "    {\"name\":\"Гранаты\", \"price\":\"400\", \"available\": 5},\n",
        "]\n",
        "\n",
        "store[0]['price'] = 150\n",
        "store[1]['price'] = 250\n",
        "store[2]['price'] = 450\n",
        "\n",
        "print(store[0])\n",
        "print(store[1])\n",
        "print(store[2])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "{'name': 'Яблоки', 'price': 150, 'available': 40}\n",
            "{'name': 'Апельсины', 'price': 250, 'available': 20}\n",
            "{'name': 'Гранаты', 'price': 450, 'available': 5}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "748Los8x_Ktl"
      },
      "source": [
        "И, конечно, если у нас есть список, мы можем запустить по нему цикл:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WlvmkMsd_mN_",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "87aa4b5d-e4ad-45f1-df71-a1e0a55e27cb"
      },
      "source": [
        "store = [\n",
        "    {\"name\":\"Яблоки\", \"price\":\"100\", \"available\": 40},\n",
        "    {\"name\":\"Апельсины\", \"price\":\"200\", \"available\": 20},\n",
        "    {\"name\":\"Гранаты\", \"price\":\"400\", \"available\": 5},\n",
        "]\n",
        "\n",
        "for fruit in store:\n",
        "  if fruit['available'] >= 6:\n",
        "    print(fruit['name'], fruit['price'])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[('Яблоки', '100'), ('Апельсины', '200')]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 129
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dm5RZOOn_wDd"
      },
      "source": [
        "### Задача. Списки словарей"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "YKxc7wceAF-g"
      },
      "source": [
        "Тотальная распродажа. Снизьте цены на все фрукты в два раза."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ICvUDPP6AJ40",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e4332179-4edf-491f-8ec6-fdf554ecd836"
      },
      "source": [
        "store = [\n",
        "    {\"name\":\"Яблоки\", \"price\":\"100\", \"available\": 40},\n",
        "    {\"name\":\"Апельсины\", \"price\":\"200\", \"available\": 20},\n",
        "    {\"name\":\"Гранаты\", \"price\":\"400\", \"available\": 5},\n",
        "]\n",
        "\n",
        "for fruit in store:\n",
        "  price = int(fruit[\"price\"])\n",
        "  new_price = price // 2\n",
        "  fruit[\"price\"] = str(new_price)\n",
        "\n",
        "\n",
        "for fruit in store:\n",
        "  print(fruit['name'], fruit['price'])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Яблоки 50\n",
            "Апельсины 100\n",
            "Гранаты 200\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}